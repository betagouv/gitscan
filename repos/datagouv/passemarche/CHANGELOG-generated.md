## Changelog : passemarche (30 derniers jours, au 12 octobre 2026)

### Résumé
Ce mois a été marqué par un développement majeur autour de la gestion des **groupements d'entreprises**. Les utilisateurs peuvent désormais composer un groupement, inviter des co-traitants, suivre l'avancement des membres via un nouveau tableau de bord et soumettre la candidature finale. L'application s'ouvre également à l'international avec l'ajout du support de la langue anglaise.

### Évolutions fonctionnelles

**Gestion des groupements et co-traitance**
- **Composition du groupement** : Le mandataire peut désormais ajouter ou retirer des co-traitants et confirmer la composition pour déclencher l'envoi des invitations [#494](https://github.com/datagouv/passemarche/pull/494).
- **Parcours d'invitation** : Amélioration du flux pour les co-traitants avec un écran d'identification dédié, une redirection fluide vers le suivi du groupement et une gestion des invitations expirées ou introuvables [#551](https://github.com/datagouv/passemarche/pull/551).
- **Nouveau tableau de bord** : Mise en place d'un tableau de bord de suivi pour le mandataire, permettant de visualiser le statut des membres, de gérer les lots et de suivre la soumission [#536](https://github.com/datagouv/passemarche/pull/536).
- **Soumission de la candidature** : Le mandataire peut désormais soumettre officiellement la candidature du groupement, avec un suivi de l'état de soumission et une gestion des erreurs via webhook [#549](https://github.com/datagouv/passemarche/pull/549).

**Gestion des lots et candidatures**
- **Mode de sélection des lots** : Introduction d'un nouveau mode de sélection des lots au sein du parcours de candidature [#504](https://github.com/datagouv/passemarche/pull/504).
- **Flexibilité des lots** : Possibilité de désactiver la limitation du nombre de lots par candidat via un indicateur de configuration [#563](https://github.com/datagouv/passemarche/pull/563).

**Internationalisation et interface**
- **Support de l'anglais** : Ajout de la langue anglaise et d'un sélecteur de langue dans l'en-tête de l'application [#538](https://github.com/datagouv/passemarche/pull/538).
- **Clarté de l'expérience** : Précision du message indiquant qu'une candidature est transmise à la plateforme de marché [#556](https://github.com/datagouv/passemarche/pull/556) et correction de plusieurs messages de confirmation.

### Évolutions techniques

**Architecture et Refactoring**
- **Composants UI** : Migration de plusieurs éléments d'interface (configuration des lots, composants de groupement) vers des `ViewComponents` pour une meilleure maintenabilité [#541](https://github.com/datagouv/passemarche/pull/541), [#540](https://github.com/datagouv/passemarche/pull/540).
- **Organisation du CSS** : Découpage du fichier `application.css` en fichiers thématiques par domaine pour simplifier la gestion des styles [#539](https://github.com/datagouv/passemarche/pull/539).
- **Logique métier** : Extraction de la logique du parcours de groupement dans un service dédié (`GroupementWizardSteps`) [#526](https://github.com/datagouv/passemarche/pull/526).

**Optimisations et Fiabilité**
- **Performance** : Résolution asynchrone des raisons sociales des membres du groupement via l'API Entreprise pour ne pas bloquer l'interface [#494](https://github.com/datagouv/passemarche/pull/494).
- **Robustesse** : Amélioration de la gestion des erreurs lors de la soumission (webhooks) et sécurisation de l'identification des co-traitants invités.

**Qualité et Développement**
- **Outils de design** : Amélioration significative des previews Lookbook pour les composants de groupement et de réponse aux attributs du marché [#542](https://github.com/datagouv/passemarche/pull/542).
- **Tests** : Augmentation de la couverture de tests via l'ajout de nombreux scénarios Cucumber couvrant les nouveaux parcours de groupement et de soumission.

### Autres changements
- Mise à jour de la configuration de l'environnement de staging pour le module groupement.
