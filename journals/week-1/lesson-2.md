# Journal: Automating Infrastructure with CloudFormation & LLM Collaboration

## Journal Summary

In this lesson, the main achievement was fully automating AWS infrastructure provisioning by authoring CloudFormation (CFN) templates for VPC, Windows and Ubuntu EC2 instances, and deploy scripts—leveraging GitHub Copilot LLM to accelerate template design and iteration. This helps with launching infrastructure resources optimally and clean resources easily once done with the experimentations

Key takeaways:

- **Prompting the LLM**: Crafted clear natural-language prompts to guide GitHub Copilot in generating parameterized CFN YAML snippets, resource definitions, outputs, and exports.
- **Template Composition**: Learned how to structure CFN templates with Parameters, Resources, Outputs, and Exports for reusable VPC and EC2 stacks.
- **IaC Best Practices**: Applied tagging conventions, default SSM AMI lookups, security group rules, and gp3 volume mappings to ensure production-readiness.
- **Deploy Automation**: Built portable Bash scripts with argument parsing, `cfn-toml`, `cfn-lint`, and `aws cloudformation deploy` commands to validate and launch stacks via CLI profiles.
- **LLM-Driven Iteration**: Embraced rapid iteration by reviewing Copilot suggestions, refining code with comments, and correcting AMI paths based on deploy errors.

Reflection:

Working alongside an LLM to scaffold and iterate IaC accelerated my understanding of AWS resource relationships and automation workflows. This collaboration model highlights how AI can complement DevOps practices, ensuring consistency and reducing manual errors as I move toward more complex infrastructure scenarios.

## Project
See full project [here](../../projects/cloud-env-setup-iac/README.md)