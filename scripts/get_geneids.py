#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import argparse
import sys
import os
import re

parser = argparse.ArgumentParser(usage='%(prog)s --file_type [gff|gtf|saf] --in_file <path/to/your/db_file>',
                                 description="This script creates three column file Gene ID, Gene Name and Gene Biotype",
                                 add_help=True
                                 )
parser.add_argument('--in_file',
                    required = True,
                    help="path to your annotation file"
                    )
parser.add_argument('--file_type',
                    required = True,
                    help="speficy file type [gff|gtf|saf]"
                    )

def get_gtf(handler):

    genes_attr = {}
    typesRegex = "\s.([A-z0-9 _. \- /\(\)]+)"
    
    for key, value in biotypes.items():
        tweak = value + typesRegex
        biotypes[key]=tweak
        
    for i in handler:
        if not i.startswith("#"):
            line = i.split('\t')
            ninthField = line[8]

            chk_gene_id = re.search('gene_id\s.([A-z0-9_-]+)', ninthField)
            chk_gene_name = re.search('gene_name\s.([A-z0-9_.:-]+)', ninthField)
    
            gene_name = 'NA'
            gene_biotype = 'NA'
            chrom = line[0]
    
            if chk_gene_name:
                gene_name = chk_gene_name.group(1)
    
            for value in biotypes.values():
                checkBiotype = re.search(value, ninthField)
                if checkBiotype:
                    gene_biotype = checkBiotype.group(1)
    
            if chrom not in genes_attr:
                genes_attr[chrom] = {}

            if chk_gene_id:
                gene_id = chk_gene_id.group(1)

                if gene_id not in genes_attr[chrom]:
                    genes_attr[chrom][gene_id] = {}
            #TODO I feel that this is error prone..
            # I'mm imaginig a situations where previous gene_name had proper value
            # but in the next iteration (next line) gene_name tag doesn't exists
            # and therefor gets NA value and thats now overides proper values already
            # stored in the dictionary
            # in theory every line in gtf files is self contained and this shouldn't happened
            # but my custome gtf violated that rule, but former lines would always hold "proper" 
            # value, so I guess I'll leave it as is for now
                genes_attr[chrom][gene_id]["gene_name"] = gene_name
                genes_attr[chrom][gene_id]["biotype"] = gene_biotype

    return genes_attr

def get_gff(handler):

    genes_attr = {}

    typesRegex = "\s.([A-z0-9 _. \- /\(\)]+)"
    
    for key, value in biotypes.items():
        tweak = value + typesRegex
        biotypes[key]=tweak
    
    for i in handler:
        line = i.strip()
        if not line.startswith('#'):
            feature = line.split('\t')
            if feature[2] == 'gene':
                ninthField = feature[8]
    
                gene_id = re.search('ID=([A-z0-9]+)', ninthField)
                chk_gene_name = re.search('Name=([A-z0-9_.:-]+)', ninthField)
    
                gene_name = 'NA'
                gene_biotype = 'NA'
                chrom = feature[0]
    
                if chk_gene_name:
                    gene_name = chk_gene_name.group(1)
    
                for value in biotypes.values():
                    checkBiotype = re.search(value, ninthField)
                    if checkBiotype:
                        gene_biotype = checkBiotype.group(1)

                if chrom not in genes_attr:
                    genes_attr[chrom] = {}

                if chk_gene_id:
                    gene_id = chk_gene_id.group(1)

                    if gene_id not in genes_attr[chrom]:
                        genes_attr[chrom][gene_id] = {}

                    genes_attr[chrom][gene_id]["gene_name"] = gene_name
                    genes_attr[chrom][gene_id]["biotype"] = gene_biotype
    
                #if gene_id:
                #    if gene_id.group(1) not in genes_attr:
                #        genes_attr[gene_id.group(1)] = []
                #        genes_attr[gene_id.group(1)].append(gene_name)
                #        genes_attr[gene_id.group(1)].append(gene_biotype)
                #        genes_attr[gene_id.group(1)].append(feature[0])
    return genes_attr

def get_saf(handler):

    genes_attr = {}

    for i in handler:
        line = i.strip()
        if line.startswith('#'):
            continue
    
        line = line.split("\t")
        gene_id = line[0]
        chrom = line[1]
        gene_name = line[5]
        biotype = line[6]
    
        genes_attr[chrom][gene_id] = {"gene_name": gene_name, "biotype": biotype}

    return genes_attr

args = parser.parse_args()
file_type = args.file_type
in_file = args.in_file

biotypes = {
    "gb": 'gene_biotype',
    "gt": 'gene_type',
    "tb": 'transcript_biotype',
    "tt": 'transcript_type'
    }

with open(in_file) as handler:
    genes_attr = None

    if file_type == "saf":
        genes_attr = get_saf(handler)
    if file_type == "gtf":
        genes_attr = get_gtf(handler)
    if file_type == "gff":
        genes_attr = get_gff(handler)

    if genes_attr is not None:
    
        header = True
        for chrom, attr in sorted(genes_attr.items()):
            if header:
                print '\t'.join(("Gene.ID", "Chrom", "Gene.Name", "Biotype"))
                header = False

            for gene_id, values in sorted(attr.items()):
                print '\t'.join((gene_id, chrom, values["gene_name"], values["biotype"]))

    else:
        sys.exit("ERROR: This should have happened. check your gene annotation and gene_idx.txt files")
