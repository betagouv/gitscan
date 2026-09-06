## Changelog : st-ansible (30 derniers jours, au 05 septembre 2026)

### Résumé
Cette période a été marquée par l'élargissement du catalogue d'applications déployables avec l'ajout de "Docs" et "Projects". Le processus de configuration initiale (bootstrap) a également été rendu plus intelligent pour mieux s'adapter aux besoins spécifiques de chaque application, évitant ainsi des configurations superflues.

### Évolutions fonctionnelles
- Ajout du support pour l'application **Projects** (fork de Planka), incluant les rôles et les commandes `st-cli` dédiés.
- Ajout du support pour l'application **Docs** (Impress), avec un nouveau rôle et une intégration complète via `st-cli`.

### Évolutions techniques
- Optimisation du processus de bootstrap : la vérification des prérequis est désormais contextuelle à l'application choisie. Cela permet d'éviter de demander la mise en place d'infrastructures inutiles (comme Redis) lorsque l'application déployée n'en a pas besoin.

### Autres changements
- Documentation de la procédure de publication (release) destinée aux mainteneurs.
- Correction mineure du rendu du fichier changelog.
