## Changelog : drive (30 derniers jours, au 04/09/2026)

### Résumé
Ce mois-ci, LaSuite Drive a considérablement renforcé la gestion de la confidentialité grâce à un nouveau système de restrictions d'accès plus flexible et granulaire. La sécurité a également été consolidée, notamment sur les flux d'édition de documents (WOPI) et la gestion des droits de suppression, tandis que la robustesse du système a été améliorée par l'intégration de nouveaux outils de tests de charge et de monitoring de performance.

### Évolutions fonctionnelles
- **Nouveau système de gestion des restrictions** : possibilité d'activer ou désactiver des restrictions, de les gérer par le déplacement de dossiers ou de cibler spécifiquement d'autres éléments.
- **Confidentialité accrue** : les éléments faisant l'objet d'une restriction sont désormais masqués dans les listes de premier niveau et sont systématiquement exclus des résultats de recherche, des exports et de l'indexation.
- **Sécurité des droits d'accès** : blocage de la suppression d'un élément par son créateur si ses droits d'accès ont été révoqués.
- **Administration** : ajout d'une fonctionnalité permettant d'abandonner manuellement une analyse de logiciel malveillant (malware) en cours.

### Évolutions techniques
- **Refonte du moteur de permissions** : restructuration du calcul des capacités (abilities) et de la résolution des rôles pour une meilleure modularité et performance.
- **Sécurisation du protocole WOPI** : implémentation de la validation de signature des requêtes, du stockage des clés de preuve client et du scan systématique des fichiers écrits via ce protocole.
- **Fiabilité et performance** : mise en place d'une suite de tests de charge (scénarios JMeter) et intégration de Sentry pour le monitoring des performances.
- **Infrastructure et CI/CD** : automatisation de la détection de malware via Helm et mise à jour des workflows de traduction (Crowdin) sur Node 22.

### Autres changements
- Mise à jour de la documentation du changelog.
- Alignement des mots de passe de démonstration avec la configuration Keycloak.
- Nettoyage et normalisation de certains fichiers de configuration (yarn.lock).
