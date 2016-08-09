 # -*- coding: utf-8 -*-

import subprocess
import shlex
import sys
import os

os.chdir('/ifs/e63data/bergerm1/Analysis/Projects/Test/tanl3/project5213')
output_dir = 'germline/gvcf/'
gatk = '/opt/common/CentOS_6-dev/gatk/GenomeAnalysisTK-3.5-0-g36282e4/GenomeAnalysisTK.jar'
reference = '/ifs/e63data/bergerm1/Resources/DMP/pubdata/hg-fasta/VERSIONS/hg19/Homo_sapiens_assembly19.fasta'

inputs = [
	'Proj_5213_I/FinalBams/s_PK_crc_021_N_bc02_Proj_5213_I_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_I/FinalBams/s_PK_crc_023_N_bc05_Proj_5213_I_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_I/FinalBams/s_PK_crc_024_N_bc07_Proj_5213_I_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_I/FinalBams/s_PK_crc_025_N_bc09_Proj_5213_I_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_I/FinalBams/s_PK_crc_026_N_bc11_Proj_5213_I_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_I/FinalBams/s_PK_crc_027_N_bc13_Proj_5213_I_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_I/FinalBams/s_PK_crc_028_N_bc15_Proj_5213_I_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_I/FinalBams/s_PK_crc_029_N_bc17_Proj_5213_I_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_I/FinalBams/s_PK_crc_030_N_bc19_Proj_5213_I_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_075_N_bc05_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_076_N_bc17_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_077_N_bc29_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_078_N_bc41_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_079_N_bc53_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_080_N_bc65_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_081_N_bc77_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_082_N_bc87_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_083_N_bc40_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_084_N_bc18_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_085_N_bc42_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_086_N_bc30_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_087_N_bc64_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_088_N_bc76_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_089_N_bc88_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_090_N_bc04_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_091_N_bc54_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_092_N_bc16_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_093_N_bc28_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_094_N_bc66_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_095_N_bc52_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_096_N_bc89_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam',
	'Proj_5213_L/FinalBams/s_PK_crc_097_N_bc06_Proj_5213_L_L000_mrg_cl_aln_srt_MD_IR_BR.bam'
]

for input_bam in inputs:
	sample_name = input_bam[22:34]
	out_gvcf = os.path.join(output_dir, sample_name + '.g.vcf')

	command = 'java -jar {gatk} -T HaplotypeCaller -R {reference} -I {input_bam} -o {out_gvcf} -ERC GVCF'.format(**locals())

	bsub = 'bsub -o germline/LSF/%J.out "{}"'.format(command)
	
	print(command)
	subprocess.call(shlex.split(bsub))

# –I sample1.bam \
# –o sample1.g.vcf \
# [ –L exome_targets.intervals \ ]
# –ERC GVCF
