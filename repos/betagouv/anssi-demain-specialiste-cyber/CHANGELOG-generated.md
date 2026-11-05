## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 04/11/2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante avec l'enrichissement des contenus sur les métiers de la cybersécurité et le lancement de la nouvelle section dédiée à la formation. L'interface a également été affinée pour offrir une expérience plus fluide, une meilleure gestion du mode sombre et une identité visuelle mise à jour.

### Évolutions fonctionnelles
- **Enrichissement de la section "Métiers"** : intégration de nouvelles données (familles de métiers, fonctions et ressources) et mise à disposition de nouvelles fonctionnalités de recherche et de consultation.
- **Lancement de la section "Se former"** : création de la page "Se former et s'entraîner en ligne" et mise en place de parcours de sélection ("Je me mesure" et "Je m'entraîne").
- **Optimisation de l'interface utilisateur** : 
    - Corrections de textes (wording) pour plus de clarté.
    - Amélioration de l'application du mode sombre.
    - Mise à jour de l'en-tête (retrait du logo et de la tagline ANSSI).
    - Gestion plus propre de l'affichage des illustrations (image générique par défaut).

### Évolutions techniques
- **Infrastructure et CI/CD** : 
    - Migration de la stack vers Node.js 26.
    - Passage de l'environnement de CI sur Ubuntu 26.04.
- **Outillage de développement** : 
    - Ajout du support Nix pour l'environnement de développement.
    - Automatisation du tri des imports.
    - Support de Vitest 5 pour les tests.
- **Architecture et Qualité** : 
    - Refactorisation du module "Métiers" pour une meilleure gestion des entités et des constructeurs.
    - Centralisation des instructions pour les agents d'IA.
    - Amélioration de la clarté et de l'explicité des tests unitaires.
    - Optimisation des logs pour le débogage de l'authentification.

### Autres changements
- **Documentation** : réorganisation complète du guide de développement.
- **Style de code** : ajustement des règles de formatage pour accepter des lignes allant jusqu'à 120 caractères.
