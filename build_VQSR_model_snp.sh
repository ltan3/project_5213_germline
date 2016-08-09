#!/bin/sh

cd /ifs/e63data/bergerm1/Analysis/Projects/Test/tanl3/project5213/germline

input="raw_germline.vcf"

hapmap="/ifs/depot/resources/gatk/bundle/2.8/b37/hapmap_3.3.b37.vcf"
omni="/ifs/depot/resources/gatk/bundle/2.8/b37/1000G_omni2.5.b37.vcf"
_1000G="/ifs/depot/resources/gatk/bundle/2.8/b37/1000G_phase1.snps.high_confidence.b37.vcf"
dbsnp="/ifs/depot/resources/gatk/bundle/2.8/b37/dbsnp_138.b37.vcf"


gatk="/opt/common/CentOS_6-dev/gatk/GenomeAnalysisTK-3.5-0-g36282e4/GenomeAnalysisTK.jar"
reference="/ifs/e63data/bergerm1/Resources/DMP/pubdata/hg-fasta/VERSIONS/hg19/Homo_sapiens_assembly19.fasta"

bsub -o LSF/%J.out -n 8 \
java -Xmx10g -jar $gatk \
    -T VariantRecalibrator \
    -R $reference \
    -input $input \
    -resource:hapmap,known=false,training=true,truth=true,prior=15.0 $hapmap \
    -resource:omni,known=false,training=true,truth=true,prior=12.0 $omni \
    -resource:1000G,known=false,training=true,truth=false,prior=10.0 $_1000G \
    -resource:dbsnp,known=true,training=false,truth=false,prior=2.0 $dbsnp \
    -an DP \
    -an QD \
    -an FS \
    -an SOR \
    -an MQ \
    -an MQRankSum \
    -an ReadPosRankSum \
    -an InbreedingCoeff \
    -mode SNP \
    -tranche 100.0 -tranche 99.9 -tranche 99.0 -tranche 90.0 \
    -recalFile vqsr/recalibrate_SNP.recal \
    -tranchesFile vqsr/recalibrate_SNP.tranches \
    -rscriptFile vqsr/recalibrate_SNP_plots.R

# https://software.broadinstitute.org/gatk/guide/article?id=2805