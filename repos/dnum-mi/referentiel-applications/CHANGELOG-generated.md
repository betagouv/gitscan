## Changelog : referentiel-applications (30 derniers jours, au 16 septembre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante en renforçant massivement sa sécurité et en introduisant des outils d'analyse avancés. Les évolutions majeures incluent le déploiement d'un moteur de détection de corrélation entre applications, la mise en place d'un centre de notifications centralisé et un durcissement global des politiques d'authentification et de gestion des droits.

### Évolutions fonctionnelles
- **Nouveautés majeures :**
    - Mise en place d'un centre de notifications avec mise à jour automatique (polling) ([#2328](https://github.com/dnum-mi/referentiel-applications/issues/2328), [#2360](https://github.com/dnum-mi/referentiel-applications/issues/2360)).
    - Déploiement d'un moteur de détection de corrélation (suggestions, scoring et interface de revue pour les administrateurs) ([#2318](https://github.com/dnum-mi/referentiel-applications/issues/2318), [#2319](https://github.com/dnum-mi/referentiel-applications/issues/2319), [#2323](https://github.com/dnum-mi/referentiel-applications/issues/2323), [#2324](https://github.com/dnum-mi/referentiel-applications/issues/2324), [#2351](https://github.com/dnum-mi/referentiel-applications/issues/2351), [#2352](https://github.com/dnum-mi/referentiel-applications/issues/2352)).
    - Lancement des campagnes d'Information Quality (IQ) ([#2350](https://github.com/dnum-mi/referentiel-applications/issues/2350), [#2439](https://github.com/dnum-mi/referentiel-applications/issues/2439)).
- **Gestion du cycle de vie des technologies :**
    - Amélioration de la visibilité sur la fin de vie (EOL) des technologies via une vue d'ensemble transversale ([#2356](https://github.com/dnum-mi/referentiel-applications/issues/2356)) et des alertes automatiques pour les propriétaires d'applications ([#2357](https://github.com/dnum-mi/referentiel-applications/issues/2357)).
    - Possibilité de définir manuellement une date de fin de vie en cas d'échec de la récupération automatique ([#2455](https://github.com/dnum-mi/referentiel-applications/issues/2455)).
    - Ajout d'une recherche spécifique pour identifier les technologies sans date de fin de vie définie ([#2660](https://github.com/dnum-mi/referentiel-applications/issues/2660)).
- **Améliorations de l'expérience utilisateur :**
    - Optimisation de la recherche avec l'ajout de filtres sauvegardés ([#2309](https://github.com/dnum-mi/referentiel-applications/issues/2309), [#2386](https://github.com/dnum-mi/referentiel-applications/issues/2386)) et un meilleur filtrage par organisation ([#2416](https://github.com/dnum-mi/referentiel-applications/issues/2416), [#2417](https://github.com/dnum-mi/referentiel-applications/issues/2417)).
    - Corrections diverses sur l'interface (tri des menus, labels, gestion des erreurs et accessibilité) ([#2537](https://github.com/dnum-mi/referentiel-applications/issues/2537), [#2566](https://github.com/dnum-mi/referentiel-applications/issues/2566), [#2570](https://github.com/dnum-mi/referentiel-applications/issues/2570), [#2616](https://github.com/dnum-mi/referentiel-applications/issues/2616)).

### Évolutions techniques
- **Sécurité et gestion des droits (Renforcement majeur) :**
    - Exigence d'une authentification forte pour l'accès aux droits élevés et l'administration ([#2625](https://github.com/dnum-mi/referentiel-applications/issues/2625), [#2630](https://github.com/dnum-mi/referentiel-applications/issues/2630)).
    - Durcissement des périmètres d'administration pour empêcher les accès transversaux non autorisés ([#2615](https://github.com/dnum-mi/referentiel-applications/issues/2615), [#2370](https://github.com/dnum-mi/referentiel-applications/issues/2370), [#2392](https://github.com/dnum-mi/referentiel-applications/issues/2392), [#2367](https://github.com/dnum-mi/referentiel-applications/issues/2367), [#2368](https://github.com/dnum-mi/referentiel-applications/issues/2368)).
    - Protection contre les injections SQL, les attaques SSRF et les failles de type IDOR ([#2366](https://github.com/dnum-mi/referentiel-applications/issues/2366), [#2373](https://github.com/dnum-mi/referentiel-applications/issues/2373), [#2496](https://github.com/dnum-mi/referentiel-applications/issues/2496)).
    - Amélioration de la traçabilité lors des sessions d'impersonation ([#2409](https://github.com/dnum-mi/referentiel-applications/issues/2409)).
- **Architecture et Backend :**
    - Optimisation de la gestion des données technologiques via le proxy d'entreprise ([#2413](https://github.com/dnum-mi/referentiel-applications/issues/2413), [#2450](https://github.com/dnum-mi/referentiel-applications/issues/2450)).
    - Amélioration de la robustesse du backend (validation des DTO, gestion des verrous de cron, idempotence des campagnes) ([#2376](https://github.com/dnum-mi/referentiel-applications/issues/2376), [#2539](https://github.com/dnum-mi/referentiel-applications/issues/2539)).
    - Alignement et automatisation du contrat OpenAPI dans le cycle de CI ([#2349](https://github.com/dnum-mi/referentiel-applications/issues/2349), [#2414](https://github.com/dnum-mi/referentiel-applications/issues/2414)).
- **Qualité et CI/CD :**
    - Renforcement de la suite de tests end-to-end (e2e) pour garantir la stabilité des fonctionnalités critiques ([#2355](https://github.com/dnum-mi/referentiel-applications/issues/2355), [#2362](https://github.com/dnum-mi/referentiel-applications/issues/2362), [#2621](https://github.com/dnum-mi/referentiel-applications/issues/2621)).
    - Validation systématique des Pull Requests sur l'ensemble des branches cibles ([#2358](https://github.com/dnum-mi/referentiel-applications/issues/2358)).
