## Changelog : transfers (30 derniers jours, au 13/10/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la sécurisation intensive de la plateforme et l'amélioration de la fiabilité des transferts. Les utilisateurs bénéficient désormais d'une meilleure gestion des téléchargements volumineux (reprise après interruption) et d'un suivi plus précis de l'état de livraison des fichiers.

### Évolutions fonctionnelles
- **Amélioration de l'expérience de téléchargement** : gestion de la reprise après interruption, affichage de la progression et meilleure gestion des erreurs (notamment pour les gros fichiers sur Firefox).
- **Suivi des envois** : affichage de l'état de livraison pour chaque destinataire afin de ne plus laisser l'utilisateur dans l'attente.
- **Interface utilisateur** : fluidification des rechargements de page et harmonisation du sélecteur d'applications (app switcher) avec le reste de la Suite.
- **Corrections de communication** : ajustement des délais annoncés dans les emails pour refléter la réalité technique.

### Évolutions techniques
- **Sécurisation renforcée** : durcissement de l'API (protection contre les attaques SSRF, gestion des jetons, limitation de débit et audit), restriction de l'accès à l'administration par liste blanche d'IP et correction de plusieurs vulnérabilités critiques (Python, Go, Django, OpenSSL).
- **Fiabilité des transferts** : sécurisation de la reprise des téléchargements via des capacités signées et amélioration de la gestion atomique des quotas de destinataires.
- **Intégration de l'analyse de sécurité** : intégration des verdicts de l'OSS Scanner et ajout de modèles de menaces (threat models).
- **Infrastructure et CI/CD** : passage aux images backend "distroless" pour réduire la surface d'attaque et mise à jour des outils de build (Caddy, lprobe).
- **Refactoring** : renommage global de l'identifiant "transferts" en "transfers" pour l'ensemble du projet.

### Autres changements
- **Documentation** : mise à jour de la politique de sécurité et de la documentation technique concernant la configuration des proxys.
