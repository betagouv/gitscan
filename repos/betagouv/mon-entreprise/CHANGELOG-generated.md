## Changelog : mon-entreprise (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, le projet a connu des évolutions majeures, notamment une refonte complète de la page d'accueil et une mise à jour approfondie des règles de calcul pour Mayotte. L'outil de comparaison a également été enrichi de nouvelles fonctionnalités de partage et d'une documentation plus accessible, tandis que le moteur de calcul a été stabilisé par un important travail de restructuration technique.

### Évolutions fonctionnelles
- **Mise en conformité pour Mayotte** : Intégration des spécificités locales dans les simulations (calcul de la Lodeom, ajustements du SMIC, cotisations sociales et avertissements spécifiques).
- **Amélioration du comparateur** : 
    - Création de liens de partage intelligents qui n'enregistrent que les modifications par rapport à la situation initiale.
    - Accès facilité à la documentation des valeurs en un seul clic.
    - Meilleure gestion du décodage des valeurs dans l'URL.
- **Refonte de l'accueil** : Nouvelle interface de la page d'accueil avec l'ajout de sections de navigation ("Qui sommes-nous", "Explorer les statuts", etc.) pour une meilleure découverte des services.
- **Nouveaux simulateurs** : Ajout des simulateurs dédiés aux profils "Artisan" et "Commerçant".

### Évolutions techniques
- **Refonte du moteur Lodeom** : Restructuration profonde du code pour améliorer la maintenabilité, incluant une meilleure organisation des domaines de calcul et une couverture de tests accrue.
- **Optimisation du comparateur** : Amélioration de la sérialisation des données et de la synchronisation entre l'interface utilisateur et l'URL.
- **Amélioration de la CI/CD** : Optimisation du workflow de revue de code par IA pour rendre les retours plus pertinents et éviter les échecs de pipeline inutiles.
- **Accessibilité et Design** : 
    - Amélioration de l'accessibilité (A11y) sur les composants de saisie.
    - Correction de contrastes de couleurs pour respecter les normes d'accessibilité (AAA).
    - Optimisation des composants de type "Card" et "Callout".

### Autres changements
- **Modernisation de la documentation** : Refonte du système de documentation utilisant MDX, permettant un rendu plus riche et une meilleure organisation des règles métier.
- **Internationalisation (i18n)** : Mise à jour et correction de nombreuses traductions sur l'ensemble de la plateforme.
- **Tests** : Renforcement significatif de la suite de tests (unitaires et intégration) sur les modules de calcul et les composants de documentation.
