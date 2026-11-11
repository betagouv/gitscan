## Changelog : labonnealternance (30 derniers jours, au 16 novembre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante dans l'automatisation de sa modération et l'amélioration de son accessibilité. Les outils de gestion ont été enrichis pour offrir un meilleur contrôle sur les offres (nouveaux écrans de modération, système d'alertes), tandis que l'expérience de recherche et les formulaires ont été affinés pour répondre aux standards de design (DSFR) et d'accessibilité (RGAA). La robustesse technique a également été renforcée par des mises à jour de sécurité et une optimisation des flux de données partenaires.

### Évolutions fonctionnelles

**Modération & Administration**
- Mise en place d'un nouvel écran de modération incluant la note de l'agent, des pastilles de conformité et une navigation facilitée entre les offres [#5911](https://github.com/mission-apprentissage/labonnealternance/issues/5911).
- Déploiement d'un socle de détection automatisé avec des règles planifiées et des alertes dédupliquées pour identifier les anomalies [#5803](https://github.com/mission-apprentissage/labonnealternance/issues/5803).
- Amélioration de la modération des offres libres avec de nouveaux verdicts de classifieur [#5745](https://github.com/mission-apprentissage/labonnealternance/issues/5745).

**Expérience utilisateur & Recherche**
- Mise en conformité avec le DSFR des champs de saisie pour le dépôt d'offres [#5854](https://github.com/mission-apprentissage/labonnealternance/issues/5854).
- Amélioration de l'accessibilité (RGAA) pour les lecteurs d'écran et la gestion des changements d'état [#5630](https://github.com/mission-apprentissage/labonnealternance/issues/5630), [#5674](https://github.com/mission-apprentissage/labonnealternance/issues/5674).
- Ajout de nouveaux filtres de recherche, notamment par OPCO [#5704](https://github.com/mission-apprentissage/labonnealternance/issues/5704).
- Optimisation du classement des résultats pour prioriser les offres à candidature simplifiée [#5851](https://github.com/mission-apprentissage/labonnealternance/issues/5851).
- Refonte de la page d'accueil "1j1s" [#5753](https://github.com/mission-apprentissage/labonnealternance/issues/5753).

**Formulaires & Contenu**
- Enrichissement des formulaires de candidatures spontanées et partenaires avec de nouvelles questions de screening [#5879](https://github.com/mission-apprentissage/labonnealternance/issues/5879).
- Intégration de formulaires de feedback utilisateurs [#5530](https://github.com/mission-apprentissage/labonnealternance/issues/5530).
- Mise à jour des éléments visuels : nouveaux logos partenaires (LinkedIn, ONISEP) [#5896](https://github.com/mission-apprentissage/labonnealternance/issues/5896) et bandeau pour les conseillers entreprise [#5907](https://github.com/mission-apprentissage/labonnealternance/issues/5907).

### Évolutions techniques

**Sécurité & Confidentialité**
- Application des correctifs de sécurité critiques pour Node.js [#5797](https://github.com/mission-apprentissage/labonnealternance/issues/5797) et Next.js [#5761](https://github.com/mission-apprentissage/labonnealternance/issues/5761).
- Renforcement de la protection des données : suppression des données personnelles envoyées à Sentry [#5701](https://github.com/mission-apprentissage/labonnealternance/issues/5701) et interdiction de loguer les JWT en clair [#5697](https://github.com/mission-apprentissage/labonnealternance/issues/5697).
- Rotation des secrets via SOPS [#5809](https://github.com/mission-apprentissage/labonnealternance/issues/5809).

**Infrastructure & Performance**
- Optimisation de la synchronisation des flux partenaires : les données ne sont retraitées que si un changement est détecté [#5834](https://github.com/mission-apprentissage/labonnealternance/issues/5834).
- Amélioration de la gestion du trafic via Nginx (limites de débit et listes de blocage) [#5777](https://github.com/mission-apprentissage/labonnealternance/issues/5777), [#5780](https://github.com/mission-apprentissage/labonnealternance/issues/5780).
- Stabilisation du processeur de tâches pour éviter les plantages mémoire sur les jobs longs [#5702](https://github.com/mission-apprentissage/labonnealternance/issues/5702).

**Observabilité & CI/CD**
- Amélioration du traçage des requêtes (reqId, trace_id) dans les logs d'accès pour faciliter le débogage [#5913](https://github.com/mission-apprentissage/labonnealternance/issues/5913).
- Optimisation de la CI : meilleure isolation des bases de données MongoDB pour les tests Vitest [#5889](https://github.com/mission-apprentissage/labonnealternance/issues/5889) et démarrage automatisé des services en environnement de test [#5892](https://github.com/mission-apprentissage/labonnealternance/issues/5892).

### Autres changements
- Nettoyage du code par la suppression de code mort [#5746](https://github.com/mission-apprentissage/labonnealternance/issues/5746).
- Maintenance de l'infrastructure de données (mise à jour de l'image Docker Metabase) [#5813](https://github.com/mission-apprentissage/labonnealternance/issues/5813).
