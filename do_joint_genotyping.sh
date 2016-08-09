#!/bin/sh

cd /ifs/e63data/bergerm1/Analysis/Projects/Test/tanl3/project5213/germline

gatk="/opt/common/CentOS_6-dev/gatk/GenomeAnalysisTK-3.5-0-g36282e4/GenomeAnalysisTK.jar"
reference="/ifs/e63data/bergerm1/Resources/DMP/pubdata/hg-fasta/VERSIONS/hg19/Homo_sapiens_assembly19.fasta"

bsub -n 8 -o LSF/%J.out "java -jar $gatk -T GenotypeGVCFs \
-R $reference \
-o ./raw_germline.vcf \
-V gvcf/s_PK_crc_021.g.vcf \
-V gvcf/s_PK_crc_023.g.vcf \
-V gvcf/s_PK_crc_024.g.vcf \
-V gvcf/s_PK_crc_025.g.vcf \
-V gvcf/s_PK_crc_026.g.vcf \
-V gvcf/s_PK_crc_027.g.vcf \
-V gvcf/s_PK_crc_028.g.vcf \
-V gvcf/s_PK_crc_029.g.vcf \
-V gvcf/s_PK_crc_030.g.vcf \
-V gvcf/s_PK_crc_075.g.vcf \
-V gvcf/s_PK_crc_076.g.vcf \
-V gvcf/s_PK_crc_077.g.vcf \
-V gvcf/s_PK_crc_078.g.vcf \
-V gvcf/s_PK_crc_079.g.vcf \
-V gvcf/s_PK_crc_080.g.vcf \
-V gvcf/s_PK_crc_081.g.vcf \
-V gvcf/s_PK_crc_082.g.vcf \
-V gvcf/s_PK_crc_083.g.vcf \
-V gvcf/s_PK_crc_084.g.vcf \
-V gvcf/s_PK_crc_085.g.vcf \
-V gvcf/s_PK_crc_086.g.vcf \
-V gvcf/s_PK_crc_087.g.vcf \
-V gvcf/s_PK_crc_088.g.vcf \
-V gvcf/s_PK_crc_089.g.vcf \
-V gvcf/s_PK_crc_090.g.vcf \
-V gvcf/s_PK_crc_091.g.vcf \
-V gvcf/s_PK_crc_092.g.vcf \
-V gvcf/s_PK_crc_093.g.vcf \
-V gvcf/s_PK_crc_095.g.vcf \
-V gvcf/s_PK_crc_096.g.vcf \
-V gvcf/s_PK_crc_097.g.vcf"