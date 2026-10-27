## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 26 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante avec le déploiement de la nouvelle section dédiée à la formation et à l'entraînement. Parallèlement, l'interface a été affinée pour améliorer la clarté du contenu et l'expérience utilisateur, tout en simplifiant l'identité visuelle du projet.

### Évolutions fonctionnelles
- **Nouvelle section de formation** : Implémentation complète de la page "Se former et s'entraîner en ligne" (route `/se-former`).
- **Améliorations de l'interface (UI/UX)** :
    - Optimisation de l'application du mode sombre.
    - Correction de l'affichage du bloc "Comment ça marche ?".
    - Utilisation d'images génériques pour pallier l'absence d'illustrations.
- **Identité et contenu** :
    - Mise à jour de l'identité visuelle avec le retrait du logo et de la tagline ANSSI.
    - Harmonisation du wording (textes) sur la page d'accueil et les sections de présentation pour plus de clarté.

### Évolutions techniques
- **Développement d'API** : Mise à disposition de nouvelles API pour les parcours "Je me mesure" et "Je m'entraîne".
- **Refactoring et optimisation** :
    - Nettoyage massif du code via la suppression de nombreuses surcharges de types inutiles (Axios, Svelte, Lodash, etc.).
    - Migration de la configuration Vitest backend vers le format ESM.
- **Expérience développeur (DevEx)** :
    - Introduction d'un shell Nix pour l'environnement de développement.
    - Automatisation du tri des imports.
- **IA et Infrastructure** :
    - Centralisation des instructions pour les agents d'intelligence artificielle.
    - Mise à jour de l'UI Kit vers la version 1.64.0.

### Autres changements
- **Documentation** : Réorganisation complète du guide de développement pour en faciliter la consultation.
