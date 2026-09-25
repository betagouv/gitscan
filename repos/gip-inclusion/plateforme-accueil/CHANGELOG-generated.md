## Changelog : plateforme-accueil (30 derniers jours, au 23 septembre 2026)

### Résumé
Ce mois-ci, la plateforme a été optimisée pour une intégration plus fluide et sécurisée en tant qu'élément embarqué (iframe). Les évolutions majeures concernent le renforcement de la sécurité des échanges, l'amélioration de la précision du suivi analytique avec la page hôte, et l'enrichissement des outils d'administration pour les gestionnaires de contenu.

### Évolutions fonctionnelles
- **Expérience utilisateur & Design** :
    - Unification de la recherche dans la section "héros" en un seul formulaire [#26].
    - Simplification visuelle de la frise de parcours par le retrait des chiffres [#41].
    - Mise à jour de la terminologie pour utiliser le terme "usager" au lieu de "candidat" [#43].
    - Ajout d'un lien direct vers le bouton de changement de mot de passe [#36].
- **Authentification** :
    - Mise en place de la connexion via le SSO [#24].
- **Administration** :
    - Amélioration du processus de duplication de contenu (choix de l'icône et redirection automatique après duplication) [#29].
    - Ajout de fonctionnalités de répétition de listes et de possibilité de téléverser des illustrations [#18].

### Évolutions techniques
- **Sécurité & Intégration (Iframe)** :
    - Durcissement de la politique de sécurité (CSP) via la définition explicite des hôtes autorisés (`frame-ancestors`).
    - Amélioration de la précision des sources des messages échangés via l'iframe [#51].
    - Optimisation du bac à sable (sandbox) de l'iframe pour permettre l'utilisation de formulaires tout en vérifiant la conformité avec la page hôte [#25].
    - Ajout de headers CORS pour les ressources nécessaires [#23].
- **Analytique & Suivi** :
    - Amélioration de la remontée de données en permettant à l'iframe de notifier la page hôte des événements et d'adopter son identité/consentement Matomo [#31].
    - Mise en place du suivi des interactions avec les sections et du déploiement de la plateforme [#32, #37].
    - Mesure de l'utilisation de chaque section via le Tag Manager [#20].
- **Performance & Infrastructure** :
    - Ajout d'un système de cache sur la page d'accueil pour optimiser les temps de chargement.
    - Ajustement des permissions de lecture pour les objets téléversés afin de les rendre publics [#19].
    - Suppression de l'utilisation d'OIDC [#34].

### Autres changements
- Documentation sur la procédure d'ouverture des ancêtres de cadres (`frame-ancestors`) lors des déploiements [#30].
