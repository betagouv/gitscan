# Bonnes pratiques CI/CD dans un contexte Github

Dans un contexte GitHub, il s'agit de définir les bonnes pratiques en terme d'organisation et d'implémentations CI/CD.

## Création d'une organisation

### Teams
Les types de Teams sont définis au niveau organisationnel afin d'avoir des modes de fonctionnement cohérent.  

| Type | Rôles |
|------|-------|
|Manager|Triage|
|TechLeads|Maintener|
|Developer| Write|

Sous la Team "Developer" on peut décliner en Team Developer Front, Team Developer Back voire en déclinant par technologies utilisées. 

### Protection Branches
Cocher les cases pour protéger la branche main

- [x] Require a pull request before merging
- [x] Require approvals
- [x] Require approval of the most recent reviewable push
- [x] Require branches to be up to date before merging
- [x] Require conversation resolution before merging 
- [x] Do not allow bypassing the above settings 
