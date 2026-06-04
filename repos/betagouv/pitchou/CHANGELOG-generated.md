## Changelog : pitchou (30 derniers jours, au 3 juin 2026)

### Résumé
Ce mois-ci, l'équipe a réalisé une refonte technique majeure de l'application, passant de Fastify et Rollup à SvelteKit et Vite pour améliorer les performances et l'expérience de développement. Des corrections de bugs et des améliorations fonctionnelles ont également été apportées, notamment au niveau de la synchronisation des dossiers, de l'interface utilisateur et de la gestion des autorisations.

### Évolutions fonctionnelles
- Ajout de liens vers les pages statistiques, budget et bouton de thème dans le footer. [#581](https://github.com/betagouv/pitchou/issues/581)
- Fusion de la page AARRI dans la page des statistiques pour une vue d'ensemble consolidée. [#582](https://github.com/betagouv/pitchou/issues/582)
- Ajout du grand capricorne à la liste des espèces protégées. [#578](https://github.com/betagouv/pitchou/issues/578)
- Ajout de seed de données pour permettre la connexion locale en développement. [#563](https://github.com/betagouv/pitchou/issues/563)
- Ajout d'un bandeau d'information sur l'environnement de staging pour une meilleure identification. [#574](https://github.com/betagouv/pitchou/issues/574)
- Ajout de la prise en charge des domaines Indre-et-Loire et Guyane pour l'authentification. [#579](https://github.com/betagouv/pitchou/issues/579)
- Autorisation des routes d'écriture et de suppression via CAP (Contrôle d'Accès Politique). [#565](https://github.com/betagouv/pitchou/issues/565)

### Évolutions techniques
- Refonte complète de l'application avec migration vers SvelteKit (SPA) et suppression de Fastify. [#566](https://github.com/betagouv/pitchou/issues/566)
- Migration du bundler Rollup vers Vite pour des temps de build plus rapides. [#564](https://github.com/betagouv/pitchou/issues/564)
- Passage à pnpm comme gestionnaire de paquets pour optimiser l'installation des dépendances. [#561](https://github.com/betagouv/pitchou/issues/561)
- Migration du code vers TypeScript pour une meilleure maintenabilité et détection d'erreurs. [#568](https://github.com/betagouv/pitchou/issues/568) et [#567](https://github.com/betagouv/pitchou/issues/567)
- Amélioration du CI/CD en utilisant `just` en local et pour les GitHub Actions. [#562](https://github.com/betagouv/pitchou/issues/562)
- Configuration d'un volume nommé pour `pgdata` dans Docker afin d'éviter les problèmes de permissions sur Linux. [#571](https://github.com/betagouv/pitchou/issues/571)
- Suppression du service `tooling` dans la configuration Docker. [#572](https://github.com/betagouv/pitchou/issues/572)

### Autres changements
- Correction d'un bug empêchant la création de décisions administratives en double. [#584](https://github.com/betagouv/pitchou/issues/584)
- Correction de l'affichage du header et du footer pour respecter les exigences de la DSFR (Design System for French Administration). [#583](https://github.com/betagouv/pitchou/issues/583)
- Correction d'un problème de rattachement des pièces jointes aux dossiers lors de la synchronisation. [#570](https://github.com/betagouv/pitchou/issues/570)
- Correction d'un bug lié à la gestion des entreprises nulles lors de la synchronisation. [#569](https://github.com/betagouv/pitchou/issues/569)
- Amélioration de la sécurité en utilisant un IV aléatoire pour le chiffrement et en durcissant la connexion et le code d'accès. [#560](https://github.com/betagouv/pitchou/issues/560) et [#557](https://github.com/betagouv/pitchou/issues/557)
- Ajout de tests unitaires avec Vitest pour la fonction `manipulationStrings`. [#559](https://github.com/betagouv/pitchou/issues/559)
- Ajout d'un shell de développement Nix et de la configuration Direnv pour un environnement de développement cohérent. [#558](https://github.com/betagouv/pitchou/issues/558)
- Ajout et application de Prettier pour formater le code de manière cohérente. [#555](https://github.com/betagouv/pitchou/issues/555)
- Correction de l'utilisation de Knex dans les migrations. [#556](https://github.com/betagouv/pitchou/issues/556)
- Correction du script de seed pour corriger l'origine des données. [#575](https://github.com/betagouv/pitchou/issues/575)
