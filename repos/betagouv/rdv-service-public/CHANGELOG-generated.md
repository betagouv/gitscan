## Changelog : rdv-service-public (30 derniers jours)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité, la performance et la sécurité de la plateforme. Plusieurs corrections de bugs ont été apportées, notamment concernant l'agenda, les webhooks et la gestion des utilisateurs. Des optimisations ont été réalisées pour améliorer la vitesse de chargement et réduire la consommation de ressources. Des mises à jour de sécurité ont également été intégrées pour protéger les données des utilisateurs.

### Évolutions fonctionnelles
- Amélioration de l'affichage des détails des rendez-vous. [#6107](https://github.com/betagouv/rdv-service-public/issues/6107)
- Possibilité de notifier les usagers d'un changement de lien de visioconférence. [#6184](https://github.com/betagouv/rdv-service-public/issues/6184)
- Ajout d'un bouton "Ajouter à mon agenda" sur l'écran de confirmation de rendez-vous. [#6190](https://github.com/betagouv/rdv-service-public/issues/6190)
- Orientation des prospects vers les services appropriés. [#6199](https://github.com/betagouv/rdv-service-public/issues/6199)
- Possibilité d'annuler une participation à un RDV collectif à l'initiative du service. [#6127](https://github.com/betagouv/rdv-service-public/issues/6127)
- Amélioration de l'affichage des prescripteurs sur les RDV collectifs. [#6124](https://github.com/betagouv/rdv-service-public/issues/6124)
- Correction de l'affichage des noms des agents superposés. [#6010](https://github.com/betagouv/rdv-service-public/issues/6010)
- Amélioration de l'affichage des erreurs lors de la saisie du code. [#6062](https://github.com/betagouv/rdv-service-public/issues/6062)
- Suppression du lien vers l'inscription. [#6216](https://github.com/betagouv/rdv-service-public/issues/6216)

### Évolutions techniques
- Migration de Webpack vers esbuild pour améliorer la performance de la compilation des assets. [#6163](https://github.com/betagouv/rdv-service-public/issues/6163)
- Passage à Yarn v4. [#6064](https://github.com/betagouv/rdv-service-public/issues/6064)
- Mise à jour de FullCalendar vers la version 6. [#6080](https://github.com/betagouv/rdv-service-public/issues/6080)
- Amélioration de la gestion des webhooks : génération asynchrone du corps et limitation des retries en cas d'erreur. [#6051](https://github.com/betagouv/rdv-service-public/issues/6051) et [#6104](https://github.com/betagouv/rdv-service-public/issues/6104)
- Optimisation de la gestion de la connexion Redis. [#6081](https://github.com/betagouv/rdv-service-public/issues/6081)
- Suppression de code obsolète lié à `oauth_applications.default_service_id`. [#6082](https://github.com/betagouv/rdv-service-public/issues/6082)
- Suppression de colonnes inutilisées dans les tables `Absences` et `Territory`. [#6092](https://github.com/betagouv/rdv-service-public/issues/6092) et [#6167](https://github.com/betagouv/rdv-service-public/issues/6167)
- Refactorisation de la gestion des exports, stockage dans Postgres. [#6213](https://github.com/betagouv/rdv-service-public/issues/6213)
- Suppression du flag `SIGN_IN_AS_ALLOWED`. [#6157](https://github.com/betagouv/rdv-service-public/issues/6157)
- Amélioration de la gestion des erreurs et des logs (Sentry). [#6097](https://github.com/betagouv/rdv-service-public/issues/6097) et [#6180](https://github.com/betagouv/rdv-service-public/issues/6180)

### Autres changements
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (CVE-2026-29063, GHSA-qffp-2rhf-9h96). [#6222](https://github.com/betagouv/rdv-service-public/issues/6222), [#6217](https://github.com/betagouv/rdv-service-public/issues/6217) et [#6218](https://github.com/betagouv/rdv-service-public/issues/6218)
- Amélioration de la documentation et des tests.
- Corrections de bugs mineurs et améliorations de l'interface utilisateur.
- Suppression de l'invitation des usagers depuis l'interface admin. [#6203](https://github.com/betagouv/rdv-service-public/issues/6203)
- Redémarrage des applications de production toutes les 2 heures. [#6215](https://github.com/betagouv/rdv-service-public/issues/6215)
- Suppression de l'ancienne colonne `caldav_disconnect_in_progress`. [#6185](https://github.com/betagouv/rdv-service-public/issues/6185)
