#!/bin/sh

cd /ifs/e63data/bergerm1/Analysis/Projects/Test/tanl3/project5213/germline

input="vqsr/recalibrated_snps_raw_indels.vcf"

dbsnp="/ifs/depot/resources/gatk/bundle/2.8/b37/dbsnp_138.b37.vcf"
mills='/ifs/depot/resources/gatk/bundle/2.8/b37/Mills_and_1000G_gold_standard.indels.b37.vcf'

gatk="/opt/common/CentOS_6-dev/gatk/GenomeAnalysisTK-3.5-0-g36282e4/GenomeAnalysisTK.jar"
reference="/ifs/e63data/bergerm1/Resources/DMP/pubdata/hg-fasta/VERSIONS/hg19/Homo_sapiens_assembly19.fasta"

bsub -o LSF/%J.out -n 8 \
java -Xmx4g -jar $gatk \
    -T VariantRecalibrator \
    -R $reference \
    -input $input \
    -resource:mills,known=true,training=true,truth=true,prior=12.0 $mills \
    -resource:dbsnp,known=true,training=false,truth=false,prior=2.0 $dbsnp \
    -an DP \
    -an QD \
    -an FS \
    -an SOR \
    -an MQRankSum \
    -an ReadPosRankSum \
    -an InbreedingCoeff \
    -mode INDEL \
    -tranche 100.0 -tranche 99.9 -tranche 99.0 -tranche 90.0 \
    --maxGaussians 4 \
    -recalFile vqsr/recalibrate_INDEL.recal \
    -tranchesFile vqsr/recalibrate_INDEL.tranches \
    -rscriptFile vqsr/recalibrate_INDEL_plots.R

# VQSR workflow
# https://software.broadinstitute.org/gatk/guide/article?id=2805

# Which resources to use
# https://software.broadinstitute.org/gatk/guide/article?id=1259 