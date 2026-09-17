## Changelog : plateforme-accueil (30 derniers jours, au 16 septembre 2026)

### Résumé
Ce mois a été marqué par une refonte majeure de l'interface d'édition (back-office) pour offrir une gestion de contenu plus intuitive et simplifiée. Parallèlement, l'expérience utilisateur a été affinée grâce à de nouveaux contenus visuels et une terminologie plus adaptée, tandis que la sécurité et les performances de l'application intégrée ont été renforcées.

### Évolutions fonctionnelles
- **Nouvelles sections de contenu** : Ajout de sections pour l'introduction, les accompagnateurs, une frise chronologique et un menu déroulant thématique.
- **Refonte de l'interface d'édition (Back-office)** :
    - Mise en place d'une interface d'édition dédiée, plus ergonomique que l'administration Django standard.
    - Possibilité d'éditer directement les en-têtes de section et d'utiliser des listes répétables avec téléchargement d'illustrations [#18].
    - Amélioration du flux de travail : sélection d'icônes avec redirection automatique après duplication [#29] et rafraîchissement immédiat de la page après sauvegarde.
- **Améliorations de l'expérience utilisateur (UX) et du design** :
    - Mise à jour visuelle du "Hero" avec des visuels haute résolution et un nouveau montage photographique.
    - Unification du formulaire de recherche dans la zone "Hero" [#26].
    - Optimisation des textes : passage du terme "candidat" à "usager" [#43], reformulation des libellés des chiffres clés et des en-têtes Emplois/Services, et suppression des tirets cadratins dans les témoignages.
    - Ajustements graphiques : retrait des chiffres de la frise de parcours [#41] et amélioration de l'espacement des éléments.
- **Corrections mineures** : Ajout d'un lien vers le bouton de changement de mot de passe [#36] et ajustement de l'affichage de la boîte de dialogue de sélection de ville.

### Évolutions techniques
- **Sécurité renforcée** :
    - Durcissement de la politique CSP (`frame-ancestors`) en listant explicitement les hôtes autorisés.
    - Ajout de headers CORS pour les ressources requises [#23].
    - Sécurisation de l'iframe via un bac à sable (sandbox) permettant l'utilisation de formulaires [#25].
    - Interdiction stricte de l'encapsulation (framing) de l'interface d'administration.
- **Authentification** : Intégration complète du SSO via Authentik [#24] et sécurisation de l'accès à l'interface d'édition via ce système.
- **Analyses et suivi** :
    - Amélioration de la remontée des événements d'analyse vers la page hôte pour un suivi plus précis.
    - Alignement de l'identité et du consentement Matomo sur ceux de la page hôte [#31].
    - Mise en place de mesures d'utilisation par section via le Tag Manager [#20].
- **Performance et Architecture** :
    - Mise en place d'un système de cache sur la page d'accueil pour accélérer le chargement.
    - Modernisation du chargement des scripts via l'utilisation des modules ES.
    - Refonte de la structure des données : les sections (frise, témoignages, parcours) sont désormais gérées comme des données structurées pour plus de flexibilité.
    - Optimisation du déploiement : automatisation des migrations et séparation des dépendances de développement du processus de production.

### Autres changements
- **Documentation** : Mise à jour de la documentation concernant la configuration des hôtes autorisés [#30], le contenu des sections et l'utilisation des scripts de suivi.
