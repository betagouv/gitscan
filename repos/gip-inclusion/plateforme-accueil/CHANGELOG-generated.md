## Changelog : plateforme-accueil (30 derniers jours, au 28 septembre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'expérience utilisateur (simplification de la recherche, ajustements de design et de terminologie) et sur le renforcement de la sécurité et des performances, notamment via l'optimisation de l'intégration en iframe et la mise en place de mécanismes de cache.

### Évolutions fonctionnelles
- **Amélioration de l'expérience utilisateur :**
    - Unification de la recherche principale dans un formulaire unique [#26](https://github.com/gip-inclusion/plateforme-accueil/issues/26).
    - Mise à jour de la terminologie pour utiliser le terme "usager" au lieu de "candidat" [#43](https://github.com/gip-inclusion/plateforme-accueil/issues/43).
    - Épuration visuelle de la frise de parcours par la suppression des chiffres [#41](https://github.com/gip-inclusion/plateforme-accueil/issues/41).
    - Correction du lien associé au bouton de changement de mot de passe [#36](https://github.com/gip-inclusion/plateforme-accueil/issues/36).

### Évolutions techniques
- **Sécurité et intégration (iframe) :**
    - Renforcement de la politique de sécurité (CSP) en listant explicitement les hôtes autorisés pour l'intégration en iframe.
    - Amélioration de la communication entre l'iframe et la page hôte (messages plus explicites [#51](https://github.com/gip-inclusion/plateforme-accueil/issues/51) et notification des événements de suivi/analytics).
    - Nettoyage des destinations de redirection sécurisées.
- **Performance et architecture :**
    - Mise en place d'un système de cache sur la page d'accueil pour optimiser les temps de chargement.
    - Suppression de l'authentification OIDC [#34](https://github.com/gip-inclusion/plateforme-accueil/issues/34) et du script `iframe-embed.js`.
    - Amélioration du suivi du déploiement de la plateforme hôte [#37](https://github.com/gip-inclusion/plateforme-accueil/issues/37).
