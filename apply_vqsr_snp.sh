#!/bin/sh

cd /ifs/e63data/bergerm1/Analysis/Projects/Test/tanl3/project5213/germline

input="raw_germline.vcf"


gatk="/opt/common/CentOS_6-dev/gatk/GenomeAnalysisTK-3.5-0-g36282e4/GenomeAnalysisTK.jar"
reference="/ifs/e63data/bergerm1/Resources/DMP/pubdata/hg-fasta/VERSIONS/hg19/Homo_sapiens_assembly19.fasta"

bsub -o LSF/%J.out -n 4 \
java -Xmx4g -jar $gatk \
    -T ApplyRecalibration \
    -R $reference \
    -input $input \
    -mode SNP \
    --ts_filter_level 99.0 \
    -recalFile vqsr/recalibrate_SNP.recal \
    -tranchesFile vqsr/recalibrate_SNP.tranches \
    -o vqsr/recalibrated_snps_raw_indels.vcf

    

# https://software.broadinstitute.org/gatk/guide/article?id=2805