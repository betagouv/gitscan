## Changelog : mobilic (30 derniers jours, au 03 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante en enrichissant les fonctionnalités pour les salariés, notamment avec la possibilité de demander un détachement ou de contester des données. L'interface a également été modernisée avec l'intégration d'un nouveau design pour l'en-tête et le pied de page, tout en améliorant la clarté de l'historique des activités et la gestion des litiges pour les administrateurs.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités :**
  - Mise en place de la demande de détachement pour les salariés ([#898](https://github.com/MTES-MCT/mobilic/pull/898)).
  - Possibilité pour les salariés d'initier une contestation de données ([#884](https://github.com/MTES-MCT/mobilic/pull/884)).
  - Ajout de la fonction d'annulation d'une mission en cours ([#889](https://github.com/MTES-MCT/mobilic/pull/889)).
- **Améliorations de l'interface (UI/UX) :**
  - Refonte visuelle de la page d'accueil avec l'intégration du nouveau header et footer conforme au DSFR ([#869](https://github.com/MTES-MCT/mobilic/pull/869), [#899](https://github.com/MTES-MCT/mobilic/pull/899), [#902](https://github.com/MTES-MCT/mobilic/pull/902)).
  - Optimisation de l'affichage des notifications, particulièrement sur les petits écrans ([#906](https://github.com/MTES-MCT/mobilic/pull/906)).
  - Amélioration de la lisibilité de l'historique des activités (harmonisation avec les PDF, meilleur espacement et textes enrichis).
  - Amélioration des outils d'administration, notamment pour la gestion des litiges et l'affichage des relevés kilométriques.
  - Simplification du parcours utilisateur par la suppression de modales d'avertissement non nécessaires.
- **Corrections :**
  - Correction du calcul du temps de validation pour les journées comportant plusieurs missions.
  - Correction de l'affichage des missions supprimées dans l'historique des salariés.

### Évolutions techniques
- **Infrastructure et CI/CD :**
  - Déploiement des "Scalingo review apps" pour faciliter les tests automatiques sur chaque Pull Request ([#904](https://github.com/MTES-MCT/mobilic/pull/904)).
  - Retour à la configuration WAF précédente pour assurer la stabilité du service ([#877](https://github.com/MTES-MCT/mobilic/pull/877)).
- **Performance et Qualité :**
  - Optimisation des appels API pour le module des webinaires ([#894](https://github.com/MTES-MCT/mobilic/pull/894)).
  - Réduction du bruit dans les rapports d'erreurs Sentry pour une meilleure surveillance ([#891](https://github.com/MTES-MCT/mobilic/pull/891)).
  - Refactorisation de composants clés de la PWA pour réduire la complexité du code et améliorer la maintenance.
- **Administration et Sécurité :**
  - Amélioration de la traçabilité et de la création de missions lors de l'utilisation du mode "impersonnalisation" ([#901](https://github.com/MTES-MCT/mobilic/pull/901), [#910](https://github.com/MTES-MCT/mobilic/pull/910)).
