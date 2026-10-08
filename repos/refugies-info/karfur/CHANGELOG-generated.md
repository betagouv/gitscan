## Changelog : karfur (30 derniers jours, au 07/10/2026)

### Résumé
Ce mois a été marqué par un développement majeur autour de l'« Espace FR », une nouvelle section dédiée à l'apprentissage du français. Parallèlement, un effort massif a été consenti pour améliorer l'accessibilité numérique du site (conformité RGAA) et renforcer la sécurité de la plateforme. L'expérience de recherche et de navigation a également été fluidifiée pour faciliter l'accès aux informations.

### Évolutions fonctionnelles
- **Lancement de l'Espace FR (Apprentissage du français) :**
    - Mise en place d'une interface complète de recherche de cours avec filtres par localisation, niveau, catégorie et public. [#3927](https://github.com/refugies-info/karfur/pull/3927)
    - Ajout d'un carrousel de cours sur la page d'accueil pour une meilleure visibilité. [#3959](https://github.com/refugies-info/karfur/pull/3959)
    - Optimisation de l'expérience mobile : filtres en plein écran, barre d'outils avec filtres actifs et gestion améliorée des résultats.
    - Nouvelles fonctionnalités de partage : partage de listes de cours via SMS et création d'une vue optimisée pour l'impression et l'export PDF. [#3943](https://github.com/refugies-info/karfur/pull/3943)
    - Affichage de nouveaux indicateurs : badges de niveau de français, mention "En ligne" pour les cours à distance et étiquettes pour les sessions imminentes.
- **Accessibilité (Conformité RGAA) :**
    - Amélioration globale de la lisibilité et du contraste des couleurs (boutons, textes, fonds de cartes) pour respecter les normes RGAA 3.2 et 3.3.
    - Optimisation de la navigation pour les lecteurs d'écran : structuration des listes, ajout d'attributs d'autocomplétion dans les formulaires et gestion des étiquettes d'erreur.
    - Amélioration de la gestion du focus et des annonces de suggestions lors de la saisie.
- **Recherche et Navigation :**
    - La barre de recherche est désormais fixe (sticky) lors du défilement pour un accès permanent. [#3913](https://github.com/refugies-info/karfur/pull/3913)
    - Amélioration de la précision des filtres de localisation (par département et par ville).
- **Interface Utilisateur :**
    - Mise à jour des logos et des sources d'information pour les partenaires (RCO, CARIF).
    - Correction de nombreux problèmes d'alignement et de design sur mobile et desktop pour correspondre aux maquettes Figma.

### Évolutions techniques
- **Sécurité :**
    - Renforcement de la sécurité contre les injections HTML en restreignant les balises autorisées par `dompurify`. [#3963](https://github.com/refugies-info/karfur/pull/3963)
    - Correction de plusieurs vulnérabilités critiques sur des dépendances clés (`next`, `image-size`, `js-yaml`, `sharp`).
- **Infrastructure et CI/CD :**
    - Ajout d'un webhook Slack pour notifier automatiquement l'équipe lors de la publication d'une nouvelle version.
    - Optimisation des processus de déploiement pour réduire les temps d'attente.
    - Migration de la configuration `pnpm` vers `pnpm-workspace.yaml`.
- **Base de données et Backend :**
    - Migration de la base de données pour inclure et mapper l'identifiant d'origine (`origin_id`) des dispositifs. [#3936](https://github.com/refugies-info/karfur/pull/3936)
    - Optimisation des performances via un audit des conversions de types dans les requêtes MongoDB. [#3961](https://github.com/refugies-info/karfur/pull/3961)

### Autres changements
- **Internationalisation (i18n) :** Mise à jour massive des traductions pour les 7 langues non-françaises, incluant la nouvelle section Espace FR.
- **Documentation :** Rédaction d'un nouveau guide de conventions de code (nommage, i18n, composants) pour harmoniser les futurs développements. [#1437](https://github.com/refugies-info/karfur/pull/3923)
- **Nettoyage :** Suppression de nombreux commentaires inutiles et de code obsolète dans l'ensemble du dépôt.
