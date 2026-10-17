## Changelog : anssi-portail (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, le portail a franchi une étape majeure dans l'accompagnement des utilisateurs avec le déploiement généralisé du "Parcours de sécurisation", qui guide désormais les organisations selon leur niveau de maturité. L'expérience interactive a été considérablement enrichie, notamment avec une refonte de la simulation "Réflexes cyber" (animations, son, score) et l'ajout de nouveaux outils pratiques dans la "Boîte à outils", comme des modèles d'annuaire de crise et des listes de contacts actualisées.

### Évolutions fonctionnelles
- **Parcours de sécurisation** : Intégration complète du parcours dans la navigation (menu, pied de page, accueil) et dans les résultats des tests pour proposer des recommandations personnalisées.
- **Simulation "Réflexes cyber"** : Amélioration de l'immersion avec l'ajout d'animations (transitions, pulsations, confettis), l'intégration du son, un nouveau système de score et une interface optimisée pour mobile et tablette.
- **Boîte à outils** : 
    - Ajout d'un outil de génération de modèle d'annuaire de crise (export XLSX).
    - Mise en place de rappels pour la mise à jour des annuaires.
    - Actualisation et enrichissement des listes de contacts (nationaux, régionaux et sectoriels).
- **Blog et contenus** : Lancement d'une nouvelle section blog avec gestion des articles, rendu optimisé et possibilité pour les utilisateurs de laisser des avis.
- **Mini-tests et simulations** : Déploiement et amélioration des tests de maturité, d'exposition et de "vrai/faux", incluant une gestion améliorée des scores et des résultats.
- **Corrections diverses** : Résolution de problèmes d'affichage (encarts, illustrations), correction de la sélection d'activités et mise à jour des statistiques (nombre d'organisations accompagnées et diagnostics réalisés).

### Évolutions techniques
- **Architecture et API** : Réorganisation profonde de la gestion des routes Express et des middlewares pour une meilleure modularité.
- **Modularisation du code** : Extraction de la logique métier dans des modules dédiés (gestion des contacts, manipulation de fichiers Excel, authentification, gestion des taux de limitation).
- **Web Components (WEBC)** : Optimisation et déploiement des mini-tests en tant que composants autonomes, avec support du mode "standalone" et gestion des ressources cross-origin.
- **Performances** : Mise en place de systèmes de cache pour les articles du blog et passage au rendu côté serveur (SSR) pour améliorer la rapidité d'affichage.
- **Infrastructure et Tooling** : Migration vers pnpm 12 et optimisation des workflows de déploiement.

### Autres changements
- **SEO et visibilité** : Mise à jour des métadonnées, des titres et des descriptions pour améliorer le référencement et le partage sur les réseaux sociaux.
- **Nettoyage** : Suppression de services obsolètes (Crisp), de commentaires inutiles et de drapeaux de fonctionnalités (feature flags) devenus inutiles.
- **Qualité éditoriale** : Corrections orthographiques, typographiques et harmonisation des libellés pour une meilleure clarté.
