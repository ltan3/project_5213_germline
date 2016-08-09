#!/bin/sh

cd /ifs/e63data/bergerm1/Analysis/Projects/Test/tanl3/project5213/germline

input="vqsr/recalibrated_snps_raw_indels.vcf"

gatk="/opt/common/CentOS_6-dev/gatk/GenomeAnalysisTK-3.5-0-g36282e4/GenomeAnalysisTK.jar"
reference="/ifs/e63data/bergerm1/Resources/DMP/pubdata/hg-fasta/VERSIONS/hg19/Homo_sapiens_assembly19.fasta"

bsub -o LSF/%J.out \
java -Xmx4g -jar $gatk \
    -T ApplyRecalibration \
    -R $reference \
    -input $input \
    -mode INDEL \
    --ts_filter_level 99.0 \
    -recalFile vqsr/recalibrate_INDEL.recal \
    -tranchesFile vqsr/recalibrate_INDEL.tranches \
    -o recalibrated_variants.vcf

    

# https://software.broadinstitute.org/gatk/guide/article?id=2805