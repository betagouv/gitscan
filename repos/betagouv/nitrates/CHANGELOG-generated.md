## Changelog : nitrates (30 derniers jours, au 21 juillet 2026)

### Résumé
Cette période a été marquée par une refonte significative de l'administration et de l'interface utilisateur, notamment pour la validation des données et le simulateur. Des améliorations de sécurité importantes ont également été apportées, avec une attention particulière à la protection contre les vulnérabilités et à la gestion des accès. Enfin, plusieurs corrections de bugs et améliorations de la qualité de vie ont été implémentées.

### Évolutions fonctionnelles
- **Administration :**
    - Ajout d'un filtre pour les données Hauts-de-France au dashboard de validation.
    - Amélioration de la recherche et de l'édition des textes conditionnels dans l'administration.
    - Ajout d'un lien d'accès rapide vers la validation des feuilles.
    - Possibilité d'éditer les libellés publics simplifiés pour les vergers et les vignes.
- **Simulateur :**
    - Amélioration de la gestion des champs de cascade et des liens directs.
    - Correction d'un bug empêchant le relancement du simulateur après une réponse.
    - Amélioration de la navigation et de l'expérience utilisateur, notamment sur mobile.
    - Suppression des éléments orphelins dans l'interface du simulateur.
- **Validation :**
    - Ajout d'un comparateur d'images empilées avec galerie de captures.
    - Amélioration du panel de détail avec auto-save htmx (plus de boutons Enregistrer).
    - Préservation du scope et de la nature lors des overrides du détail.
    - Ajout d'un lien vers le viewer YAML pour les arbres PAR et ZAR.
- **Calendrier :**
    - Amélioration de l'affichage et de la justification des périodes.
    - Correction de l'overflow des dates sur le calendrier.
    - Affichage des mois en abrégé sur mobile.

### Évolutions techniques
- **Sécurité :**
    - Correction d'une vulnérabilité de type reflected-XSS dans l'administration.
    - Mise à jour des dépendances pour corriger des vulnérabilités (high, critical, medium).
    - Renforcement de la sécurité de la page de login admin, désactivation du mot de passe par défaut et utilisation de ProConnect.
    - Protection contre le contournement de ProConnect via le fallback mot de passe admin.
- **Infrastructure & CI/CD :**
    - Mise en place d'un workflow CI/CD pour l'environnement de développement.
    - Exclusions des applications Envergo non-nitrates de la couverture de code.
    - Migration et seeding de la base de données avant les garde-fous GitOps.
    - Déclenchement du CI également sur la branche `develop`.
- **Tests :**
    - Réalignement des tests Playwright sur l'état actuel du simulateur.
    - Mise à jour des tests pour refléter les changements dans les données.
- **Architecture :**
    - Suppression du fichier `referentiels.yaml` et utilisation d'un seeding natif de la base de données.
    - Amélioration de la gestion des arbres actifs et des snapshots.

### Autres changements
- Documentation : Mise à jour des textes de contenu avec la nouvelle version.
- Correction de problèmes de style et de grammaire dans le code.
- Amélioration de l'accessibilité du simulateur.
- Ajustements de l'interface utilisateur pour le thème sombre.
- Diverses corrections de bugs et améliorations de la qualité du code.
- Mise à jour des dépendances de développement (actions/setup-python).
