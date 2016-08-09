# project_5213_germline

8/9/16 Lance Tan

Working directory for project is `/ifs/e63data/bergerm1/Analysis/Projects/Test/tanl3/project5213/germline` on luna server.

I ran scripts/commands,  in this order:

1) `do_germline_calling.py` (Call variants on each sample using HaplotypeCaller)
   - Created one genomic vcf for each sample in `gvcf/`
   - One sample was excluded (moved to `gvcf_mismatched_normal/`) because it was 
     from a mismatched tumor/normal pair

2) `do_joint_genotyping.sh` (Combine genomic vcfs into one big raw vcf file)
   - `raw_germline.vcf`

3) `build_VQSR_model_snp.sh` (Create VQSR model for SNPs, VariantRecalibrator)
   - Output is in `vqsr/`

4) `apply_VQSR_snp.sh` (Apply model, ApplyRecalibration)
   - Created `vqsr/recalibrated_snps_raw_indels.vcf`, VCF with only SNPs recalibrated

5) `build_VQSR_model_indel.sh`
   - Output is in `vqsr/`

6) `apply_VQSR_indel.sh`
   - Created `recalibrated_variants.vcf`, VCF with all SNPs/indels recalibrated

7) Apply some hard filters: `filter.py recalibrated_variants.vcf filtered.vcf`
   - Kept all events that were 'PASS' and had >= 3 samples with DP > 20, 
     largest VF > .25
   - Output to `filtered.vcf`

8) Run `cmo_vcf2maf` on that, to get annotations
   - Output to filtered.maf
