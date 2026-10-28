## Changelog : catalogi (30 derniers jours, au 23 octobre 2026)

### Résumé
Cette période a été marquée par une refonte de l'interface de consultation des logiciels et une amélioration majeure de la manière dont l'application récupère et traite les données provenant de sources externes. La sécurité de l'authentification et la robustesse de l'importation de données ont également été renforcées pour garantir la fiabilité du catalogue.

### Évolutions fonctionnelles
- **Refonte de la page de détails des logiciels** : passage à un affichage en page unique avec une navigation latérale pour faciliter la lecture et l'accès aux différentes sections.
- **Amélioration de l'ergonomie** : polissage de la navigation et restauration de contenus sur les pages de détails.

### Évolutions techniques
- **Gestion des données et sources** :
    - Amélioration de l'importation des sources externes (gestion des priorités par catégorie, fusion des textes localisés par langue et meilleure correspondance des identifiants).
    - Automatisation de la création de sources de "forges" à partir des identifiants de dépôts.
    - Amélioration de l'exportation au format Codemeta (export de la base de données et ajout de versioning).
    - Optimisation de la détection des licences de logiciels libres via Wikidata.
- **Sécurité et Infrastructure** :
    - Correction d'une vulnérabilité sur le flux d'authentification OIDC (liaison des transactions au navigateur initiateur).
    - Mise à jour de l'environnement Node.js vers une version sécurisée (24.22.1).
    - Mise en place d'un environnement de test de pénétration (pentest) local.
- **Qualité et Tests** :
    - Renforcement des tests de bout en bout (E2E) pour valider le nouveau parcours de consultation.
    - Ajout de scripts pour le peuplement de la base de données (seeding) afin de faciliter les tests et le développement.

### Autres changements
- Mise à jour de la documentation de déploiement.
- Nettoyage de la configuration de l'interface utilisateur lors des nouvelles installations.
