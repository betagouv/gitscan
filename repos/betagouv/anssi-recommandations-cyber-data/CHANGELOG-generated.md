## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 03/11/2026)

### Résumé
Ce mois-ci, le projet a gagné en autonomie grâce à la possibilité de lancer les évaluations du modèle C4 directement depuis l'interface utilisateur. Des interventions techniques ont également permis de stabiliser les processus de test automatique et de renforcer la sécurité du système.

### Évolutions fonctionnelles
- Lancement des évaluations du modèle C4 désormais accessible directement via l'interface utilisateur (au lieu de passer par GitHub Actions).

### Évolutions techniques
- CI/CD : Migration du déclenchement des évaluations du modèle C4 de GitHub Actions vers l'interface utilisateur.
- CI/CD : Correction de la configuration Python pour garantir le bon fonctionnement de la chaîne d'intégration continue.
- Environnement : Mise à jour de Node.js vers la version 24.22.1.
- Sécurité : Mise à jour de la bibliothèque Pillow (v13.0.0) pour corriger des vulnérabilités.

### Autres changements
- Documentation : Ajout d'un modèle C4 pour MQC-Data.
