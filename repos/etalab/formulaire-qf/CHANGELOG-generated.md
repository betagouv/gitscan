## Changelog : formulaire-qf (30 derniers jours, au 06 novembre 2026)

### Résumé
Ce mois a été marqué par un effort important de sécurisation des données personnelles et de stabilisation du parcours usager. Les corrections apportées visent principalement à améliorer la fiabilité des échanges avec FranceConnect et HubEE, tout en garantissant qu'aucune donnée sensible ne soit accidentellement enregistrée dans les outils de suivi technique (Sentry).

### Évolutions fonctionnelles
- **Amélioration du parcours usager :**
  - Correction de bugs lors de l'utilisation de FranceConnect pour assurer une redirection fluide ([#419](https://github.com/etalab/formulaire-qf/pull/409), [#413](https://github.com/etalab/formulaire-qf/pull/413)).
  - Correction du bouton de retour vers le site de la collectivité ([#412](https://github.com/etalab/formulaire-qf/pull/412)).
  - Amélioration de la gestion des erreurs de transmission : affichage de pages d'échec explicites lorsque le service HubEE ne répond pas ([#412](https://github.com/etalab/formulaire-qf/pull/404), [#408](https://github.com/etalab/formulaire-qf/pull/408)).
- **Fiabilisation des données :**
  - Correction de la gestion des numéros de dossier pour les collectivités ([#410](https://github.com/etalab/formulaire-qf/pull/410)).
  - Résolution de problèmes liés aux numéros de téléphone manquants ou mal formatés ([#422](https://github.com/etalab/formulaire-qf/pull/422), [#405](https://github.com/etalab/formulaire-qf/pull/405)).
  - Correction des références de confirmation et des pages de transmission ([#413](https://github.com/etalab/formulaire-qf/pull/403), [#411](https://github.com/etalab/formulaire-qf/pull/402)).

### Évolutions techniques
- **Sécurité et protection des données :**
  - **Confidentialité :** Suppression massive des données sensibles (identités, réponses API, emails de collectivités) des rapports d'erreurs Sentry pour garantir la conformité RGPD ([#406](https://github.com/etalab/formulaire-qf/pull/406), [#393](https://github.com/etalab/formulaire-qf/pull/393)).
  - **Correctifs de sécurité :** Mise à jour de dépendances critiques pour corriger des vulnérabilités (Rack, Addressable, Loofah, Crass) ([#420](https://github.com/etalab/formulaire-qf/pull/420), [#424](https://github.com/etalab/formulaire-qf/pull/424), [#416](https://github.com/etalab/formulaire-qf/pull/416)).
- **Maintenance et infrastructure :**
  - **Montée de version majeure :** Passage à Ruby 4.0.9 et Rails 8.1.4.1.
  - **Gestion des tâches :** Mise à jour de GoodJob pour la gestion des processus en arrière-plan ([#430](https://github.com/etalab/formulaire-qf/pull/430)).
  - **Optimisation CI/CD :** Amélioration de la concurrence des tests et automatisation des tests sur chaque pull request.
  - **Développement :** Suppression de Spring pour simplifier l'environnement de travail local.

### Autres changements
- **Documentation :** Mise à jour du fichier `CLAUDE.md` pour inclure les commandes et conventions de développement du projet.
- **Outils de développement :** Ajout de scripts pour faciliter l'utilisation des `worktrees` et la gestion des bases de données locales.
