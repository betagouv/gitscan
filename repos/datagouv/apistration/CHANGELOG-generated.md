## Changelog : apistration (30 derniers jours, au 02 octobre 2026)

### Résumé
Ce mois-ci, Apistration a franchi des étapes importantes avec l'intégration de la gestion DataPass, une refonte majeure de la documentation des erreurs pour faciliter le travail des développeurs, et un renforcement significatif de la sécurité via de nouveaux mécanismes d'introspection de jetons et de contrôle d'accès par adresse IP.

### Évolutions fonctionnelles
- **Intégration de DataPass** : gestion complète du cycle de vie des demandes, authentification et consultation des formulaires associés [#455](https://github.com/datagouv/apistration/pull/455).
- **Amélioration de la gestion des erreurs** : mise en place d'une nouvelle nomenclature des codes d'erreur, désormais exposée dans la documentation et les SDK pour simplifier le diagnostic des développeurs [#395](https://github.com/datagouv/apistration/pull/395), [#456](https://github.com/datagouv/apistration/pull/456).
- **Évolutions EAJE** : support de l'attestation vérifiable via PDF et intégration de preuves d'attestation sécurisées dans les jetons [#427](https://github.com/datagouv/apistration/pull/427).
- **Interface utilisateur** : ajout des logos institutionnels (data.gouv.fr et numerique.gouv.fr) en pied de page [#452](https://github.com/datagouv/apistration/pull/452) et optimisation de la lisibilité des tableaux de bord et des pages de vérification.

### Évolutions techniques
- **Sécurité des jetons** : déploiement d'un nouvel endpoint d'introspection de jeton (v3) et mise à jour automatique des SDK officiels [#415](https://github.com/datagouv/apistration/pull/415).
- **Contrôle d'accès renforcé** : imposition de plages d'adresses IP pour les jetons "éditeur" [#464](https://github.com/datagouv/apistration/pull/464) et obligation d'une date d'expiration pour tous les jetons [#459](https://github.com/datagouv/apistration/pull/459).
- **Résilience de l'authentification** : automatisation de la rotation des mots de passe pour le fournisseur INSEE afin de limiter les risques d'incident [#383](https://github.com/datagouv/apistration/pull/383).
- **Observabilité et conformité** : filtrage des données personnelles sensibles (dates et lieux de naissance) dans les logs et optimisation du suivi des erreurs via Sentry.
- **Infrastructure et CI/CD** : amélioration des workflows de test (utilisation de worktrees) et flexibilité accrue des cibles de déploiement sur GitHub Actions.

### Autres changements
- **Documentation** : mises à jour importantes des guides techniques (CNAV, INSEE, procédures de rotation et nomenclature des erreurs).
- **Maintenance** : nettoyage du code, suppression d'exemples de tests obsolètes et mise à jour de la compatibilité JSON 3.
