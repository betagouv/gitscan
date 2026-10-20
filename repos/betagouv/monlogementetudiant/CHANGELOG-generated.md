## Changelog : monlogementetudiant (30 derniers jours, au 19 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante avec l'introduction d'un système complet de gestion des tickets de support, permettant aux étudiants de signaler des problèmes et aux administrateurs de les traiter efficacement. Parallèlement, un effort majeur a été porté sur le renforcement de la sécurité des données et de l'accès, ainsi que sur l'amélioration de l'expérience de recherche et de gestion pour les étudiants et les gestionnaires de résidences.

### Évolutions fonctionnelles
- **Système de support et signalement** :
    - Mise en place d'un formulaire de signalement de problèmes pour les étudiants.
    - Création d'une interface d'administration dédiée pour gérer les tickets (vue liste, détails, catégories et statuts).
    - Ajout de notifications par email pour le suivi des tickets et les alertes quotidiennes pour les gestionnaires.
- **Expérience Étudiant** :
    - Ajout d'objectifs personnalisés dans le plan d'action étudiant.
    - Possibilité de sauvegarder les calculs budgétaires et de les télécharger au format PDF.
    - Amélioration de la recherche avec la géolocalisation et stabilisation de la carte des résultats.
    - Ajout de fonctionnalités de zoom/dézoom sur la carte.
- **Gestion pour les propriétaires et gestionnaires** :
    - Amélioration de la gestion des contacts (export CSV, suivi, et gestion des modes de contact).
    - Possibilité pour les propriétaires d'afficher un numéro de téléphone sur les pages de résidence.
    - Affichage de la date de dernière mise à jour des disponibilités dans l'espace propriétaire.
    - Nouvelles fonctionnalités de suspension des candidatures.
- **Interface et Ergonomie** :
    - Refonte de l'interface de recherche et de l'UI globale.
    - Remplacement des sélecteurs de bourses/logement par des boutons radio (Oui/Non) pour plus de clarté.
    - Ajout d'une page de changelog pour les administrateurs.

### Évolutions techniques
- **Sécurité et Protection des données** :
    - Renforcement massif de la sécurité : implémentation d'une politique de sécurité de contenu (CSP) stricte, hachage des jetons de vérification et des liens magiques, et masquage des erreurs SQL en production.
    - Durcissement des accès : restriction des routes API, limitation des tailles de requêtes tRPC et sécurisation des redirections.
    - Nettoyage des sessions : purge automatique des tentatives de connexion échouées et des jetons expirés.
- **Base de données et Performance** :
    - Création du schéma et des migrations pour la gestion des tickets de support.
    - Optimisation des performances via l'ajout d'index sur les identifiants utilisateurs et les événements de suivi.
    - Normalisation des adresses e-mail pour éviter les doublons.
- **Qualité logicielle et Infrastructure** :
    - Montée de version de Next.js.
    - Refactorisation des formulaires de connexion avec `react-hook-form`.
    - Augmentation significative de la couverture de tests (unitaires et intégration) sur le nouveau système de tickets.
    - Transition de la limitation de débit (rate limiting) vers un WAF en amont.

### Autres changements
- **Nettoyage du code** : suppression des références et des identifiants liés à l'ancien système Django et retrait des commentaires obsolètes ou redondants.
- **Accessibilité et Contenu** : mise à jour de la terminologie pour l'accessibilité (ex: "adapté PMR") et ajout de traductions (i18n).
- **Modernisation** : passage des illustrations budgétaires au format SVG et suppression des correctifs spécifiques à Internet Explorer.
