## Changelog : mesads (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives pour les administrateurs et les inspecteurs.  De nouvelles fonctionnalités facilitent l'import de données, la gestion des véhicules relais et le suivi des autorisations de stationnement. Une attention particulière a été portée à la sécurité avec la correction d'une faille potentielle.

### Évolutions fonctionnelles
- Ajout d'une vue d'import d'ADS (Autorisations de Stationnement) accessible depuis l'interface d'administration. [#142](https://github.com/MTES-MCT/mesads/pull/142)
- Les préfectures peuvent désormais modifier et supprimer les véhicules relais. [#138](https://github.com/MTES-MCT/mesads/pull/138)
- Amélioration de la recherche dans le parcours inspecteur. [#137](https://github.com/MTES-MCT/mesads/pull/137)
- Ajout d'une colonne "statut" dans le tableau des ADS du parcours inspecteur, indiquant si les informations sont complètes, incomplètes ou obsolètes. [#140](https://github.com/MTES-MCT/mesads/pull/139)
- Mise en place d'une gestion de listes d'attentes séparées pour les EPCI (Établissements Publics de Coopération Intercommunale). [#149](https://github.com/MTES-MCT/mesads/pull/149)
- Ajout d'un service et d'une commande pour l'import d'ADS. [#139](https://github.com/MTES-MCT/mesads/pull/139)
- Ajout de notifications automatiques pour inciter à la vérification et au completage des informations. [#149](https://github.com/MTES-MCT/mesads/pull/149)

### Évolutions techniques
- Correction d'une faille de sécurité potentielle liée à l'exécution de JavaScript non sécurisé. [#149](https://github.com/MTES-MCT/mesads/pull/149)
- Utilisation de `format_html` pour prévenir l'exécution involontaire de JavaScript.
- Correction d'un problème de sérialisation des enums dans les tests. [#143](https://github.com/MTES-MCT/mesads/pull/143)

### Autres changements
- Aucun changement significatif à signaler.
