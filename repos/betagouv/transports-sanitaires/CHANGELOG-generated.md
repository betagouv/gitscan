## Changelog : transports-sanitaires (30 derniers jours, au 18/08/2026)

### Résumé
Le projet a franchi une étape importante avec l'intégration des nouvelles règles métier (v8.10) et l'ajout de la génération automatique de formulaires CERFA pré-remplis. Parallèlement, une refonte structurelle majeure a été réalisée pour simplifier l'organisation du code et regrouper les outils de test et de développement.

### Évolutions fonctionnelles
- **Mise à jour des règles métier** : Intégration de la version 8.10 incluant les nouvelles cibles, les prestations et l'application de l'Article 80 différencié.
- **Génération de documents** : Possibilité de générer et de télécharger une prescription CERFA pré-remplie directement à la fin du parcours de simulation.
- **Outils de test et de consultation** : Création d'un catalogue de situations de référence ("seeds") permettant de consulter et de tester des cas types.
- **Analyse de données** : Amélioration des exports Excel pour l'analyse de données (format plateforme-finess avec détails par territoire).
- **Correction de bug** : Correction d'une erreur de terminologie où le terme "transports itératifs" était utilisé à la place de "transport en série".

### Évolutions techniques
- **Refonte de l'architecture** : Réorganisation profonde du simulateur pour regrouper les modes de développement et de laboratoire sous une interface unique d'« outils produit ».
- **Modularité du code** : Restructuration des modules front-end (fusion des modules d'identification) et découpage de composants complexes pour améliorer la maintenance.
- **Standardisation** : Harmonisation du nommage des fichiers composants (`.tsx`) en UpperCamelCase.
- **Sécurisation** : Restriction du téléchargement des documents CERFA aux seuls outils de production.

### Autres changements
- **Documentation** : Mise à jour du schéma de fonctionnement détaillant l'interaction entre les outils et le processus de génération du CERFA.
