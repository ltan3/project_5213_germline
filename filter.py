from __future__ import division
import vcf
import sys
import argparse

'''
Filters:
0) no FILTER flag (not filtered out by VQSR)
1) Minimum total read depth
2) Minimum variant allele fraction (for locations with multiple 
   alternate alleles, compare to the maximum VF)
3) Mininum number of samples that need to pass the above
'''

def filter_vcf(vcf_reader, args):

  MIN_DP = args.min_dp 
  MIN_VF = args.min_vf 
  MIN_SAMPLES = args.min_samples 

  for record in vcf_reader:
    # `record` is a vcf.model._Record

    if not record.FILTER:
      samples = record.samples
      present_count = 0
      
      for sample in samples:
        # `sample` is a vcf.model._Call

        ad = sample.data.AD # Ref, alt, [alt2, ...] allele depth
        alt = max(ad[1:]) # Maximum alt allle depth
        dp = sample.data.DP # Total read depth

        if dp and dp > MIN_DP and alt / dp > MIN_VF:
          present_count += 1

      if present_count >= MIN_SAMPLES:
        yield record


def main(*args):
  parser = argparse.ArgumentParser()
  
  parser.add_argument('in_vcf', metavar = 'in.vcf')
  parser.add_argument('out_vcf', metavar = 'out.vcf')

  parser.add_argument('--min-dp', type = int, default = 20)
  parser.add_argument('--min-vf', type = float, default = .25)
  parser.add_argument('--min-samples', type = int, default = 3)

  args = parser.parse_args(args) if args else parser.parse_args()

  in_path = args.in_vcf
  out_path = args.out_vcf

  with open(in_path, 'rU') as in_p, open(out_path, 'w') as out_p:
    reader = vcf.Reader(in_p)
    writer = vcf.Writer(out_p, template=reader)

    for record in filter_vcf(reader, args):
      writer.write_record(record)

if __name__ == '__main__':
  main()

