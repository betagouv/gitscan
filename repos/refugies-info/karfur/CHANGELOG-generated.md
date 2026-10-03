## Changelog : karfur (30 derniers jours, au 02 octobre 2026)

### Résumé
Ce mois a été marqué par le développement majeur de l'**Espace FR**, une nouvelle section dédiée à l'apprentissage du français. Cette évolution apporte des outils de recherche complets, des filtres par niveau et localisation, ainsi qu'une expérience optimisée sur mobile. Parallèlement, un effort massif a été consenti pour améliorer l'accessibilité numérique (conformité RGAA) et renforcer la qualité des traductions pour les utilisateurs non-francophones.

### Évolutions fonctionnelles
- **Lancement de l'Espace Apprentissage du Français (Espace FR) :**
    - Mise en place d'un moteur de recherche de cours avec filtres avancés (localisation, niveau de langue, catégorie et public cible). [#3927](https://github.com/refugies-info/karfur/issues/3927)
    - Ajout d'un carrousel de cours sur la page d'accueil et de nouveaux onglets de navigation (cours à venir, à la demande, tous les cours). [#3959](https://github.com/refugies-info/karfur/issues/3959)
    - Optimisation de l'interface mobile : barre d'outils dédiée, filtres en plein écran et mise en page des fiches de cours adaptée aux petits écrans.
    - Nouvelles options de consultation : possibilité de partager des cours par SMS et création d'une vue dédiée pour l'impression/export PDF.
- **Amélioration de la recherche et de l'affichage :**
    - Ajout de badges visuels pour identifier rapidement les cours "En ligne" ou les niveaux de français.
    - Amélioration de la barre de recherche générale (mode "sticky" pour rester visible au scroll).
    - Affichage de nouveaux indicateurs comme la mention "Début prochainement" pour les sessions imminentes.
- **Internationalisation :**
    - Extension et correction des traductions dans les 7 langues disponibles, assurant une cohérence sur l'ensemble des nouveaux contenus.

### Évolutions techniques
- **Accessibilité (Conformité RGAA) :**
    - Mise en conformité majeure des composants pour les lecteurs d'écran : structuration sémantique des listes (départements, publics, contacts), gestion du focus lors des recherches et des modales, et amélioration de la navigation clavier.
    - Amélioration de l'accessibilité des formulaires (attributs autocomplete, labels explicites et gestion des messages d'erreur).
- **Base de données et Backend :**
    - Évolution du schéma de données pour inclure des identifiants courts (`short name`) et des références d'origine (`origin_id`) pour les besoins et dispositifs.
    - Correction de problèmes de typage avec MongoDB.
- **Sécurité :**
    - Mise à jour de dépendances critiques pour corriger des vulnérabilités (notamment sur le package `image-size`).

### Autres changements
- **Qualité et Workflow :**
    - Rédaction et intégration d'un document de conventions de code pour harmoniser les développements de l'équipe.
    - Optimisation du workflow de revue de code via l'amélioration des processus de CI/CD.
    - Migration de la configuration de gestion de projet vers `pnpm-workspace.yaml`.
