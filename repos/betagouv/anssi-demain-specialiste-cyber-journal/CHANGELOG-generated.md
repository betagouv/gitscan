## Changelog : anssi-demain-specialiste-cyber-journal (30 derniers jours, au 18 juillet 2026)

### Résumé
Ce journal des événements métiers pour DemainSpécialisteCyber a bénéficié d'améliorations de sécurité au niveau de l'intégration continue (CI). Les configurations sont maintenant validées et les identifiants Git sont désactivés lors du clonage des dépôts, renforçant ainsi la protection des informations sensibles. La configuration de Renovate a également été initialisée pour la gestion des dépendances.

### Évolutions techniques
- Sécurité : Désactivation des identifiants Git lors du clonage des dépôts dans les workflows CI. [#SECURITE][CI] ea74175
- Sécurité : Validation des configurations dans les workflows CI. [#SECURITE][CI] 87bcd76
- Intégration Continue : Configuration initiale de Renovate pour la gestion automatisée des dépendances. 785b75c

### Autres changements
- Ajout du fichier de configuration Renovate (`renovate.json`). d23eaaa
