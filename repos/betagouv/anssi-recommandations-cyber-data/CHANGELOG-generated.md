## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 03/11/2026)

### Résumé
Les évolutions récentes permettent désormais de lancer les évaluations du modèle directement depuis l'interface utilisateur, offrant plus de flexibilité. Le projet a également bénéficié de renforcements de sécurité et d'une stabilisation des environnements de développement et de déploiement.

### Évolutions fonctionnelles
- Possibilité de déclencher les évaluations du modèle C4 directement depuis l'interface utilisateur (au lieu de passer par les processus automatisés de GitHub).

### Évolutions techniques
- CI/CD : Migration du mécanisme de lancement des évaluations de GitHub Actions vers l'interface applicative.
- CI/CD : Stabilisation de la chaîne d'intégration continue via la mise à jour des versions de Python et Node.js.
- CI/CD : Optimisation de la gestion des Pull Requests liées aux mises à jour de dépendances.
- Sécurité : Mise à jour de la bibliothèque Pillow (v13.0.0) pour corriger des vulnérabilités.

### Autres changements
- Documentation : Ajout d'un modèle C4 pour MQC-Data.
