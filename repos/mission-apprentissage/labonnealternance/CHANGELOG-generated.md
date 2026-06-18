## Changelog : labonnealternance (30 derniers jours, au 17 juin 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de la plateforme, notamment des optimisations pour le SEO, des corrections de bugs impactant l'expérience utilisateur (affichage, soumission de candidatures, etc.) et des améliorations techniques pour la stabilité et la performance. Des migrations d'infrastructure ont également été réalisées pour préparer l'avenir de la plateforme.

### Évolutions fonctionnelles
- **SEO :** Ajout de pages métiers optimisées pour le référencement ([#3222](https://github.com/mission-apprentissage/labonnealternance/issues/3222)).
- **Offres d'emploi :**
    - Correction d'un bug empêchant la mise à jour de la description des offres ([#4804](https://github.com/mission-apprentissage/labonnealternance/issues/4804)).
    - Amélioration de la gestion des offres d'emploi désactivées, avec une restauration des offres impactées ([#4813](https://github.com/mission-apprentissage/labonnealternance/issues/4813)).
    - Correction de l'affichage du niveau de diplôme visé, maintenant correctement mappé à la qualification d'emploi France Travail ([#4819](https://github.com/mission-apprentissage/labonnealternance/issues/4819)).
    - Application du seuil de 80 candidatures aux offres partenaires en "smart apply" ([#4799](https://github.com/mission-apprentissage/labonnealternance/issues/4799)).
- **Candidatures :**
    - Amélioration de l'UX du formulaire de prise de RDV CFA ([#4773](https://github.com/mission-apprentissage/labonnealternance/issues/4773)).
    - Ajout d'un focus et d'un scroll sur le premier champ en erreur lors de la soumission du formulaire de candidature ([#4771](https://github.com/mission-apprentissage/labonnealternance/issues/4771)).
- **Interface utilisateur :** Renommage du libellé du filtre "candidatures spontanées" en "entreprise à contacter" ([#4797](https://github.com/mission-apprentissage/labonnealternance/issues/4797)).
- **Handimatch :** Ajout du SIRET Handimatch pour une meilleure intégration ([#3171](https://github.com/mission-apprentissage/labonnealternance/issues/3171)).
- **CTA :** Modification des CTA (boutons d'appel à l'action) de dépôt d'offre ([#3136](https://github.com/mission-apprentissage/labonnealternance/issues/3136)).

### Évolutions techniques
- **Infrastructure :** Migration des serveurs lba-preview et lba-recette ([#4829](https://github.com/mission-apprentissage/labonnealternance/issues/4829), [#4828](https://github.com/mission-apprentissage/labonnealternance/issues/4828)).
- **Logging :** Unification du logging sur Pino avec corrélation reqId et enrichissement des logs HTTP ([#4800](https://github.com/mission-apprentissage/labonnealternance/issues/4800)).
- **Suppression de code :** Suppression des sous-modules `.infra/authorizations` et `.infra/inventories` ([#4825](https://github.com/mission-apprentissage/labonnealternance/issues/4825)).
- **Mise à jour de dépendances :** Mise à jour de Next.js ([#4730](https://github.com/mission-apprentissage/labonnealternance/issues/4730)).
- **Sécurité :** Configuration du merge driver sops pour les fichiers d'environnement chiffrés ([#4736](https://github.com/mission-apprentissage/labonnealternance/issues/4736)).
- **API :** Suppression de Swagger et de ses dépendances de l'API v1 ([#4717](https://github.com/mission-apprentissage/labonnealternance/issues/4717)).

### Autres changements
- **Documentation :** Suppression des scripts Biome redondants et mise à jour de la documentation ([#4761](https://github.com/mission-apprentissage/labonnealternance/issues/4761)).
- **Configuration :** Amélioration des notifications Slack MEP et release (Block Kit) ([#4751](https://github.com/mission-apprentissage/labonnealternance/issues/4751)).
- **Gestion des issues :** Modernisation des templates d'issues et migration des références Jira vers GitHub Issues ([#4698](https://github.com/mission-apprentissage/labonnealternance/issues/4698)).
- **Génération de fichiers :** Génération d'un fichier `llms.txt` à la racine du site ([#4765](https://github.com/mission-apprentissage/labonnealternance/issues/4765)).
- **Divers :** Suppression de la fonte Marianne Medium inutilisée ([#4762](https://github.com/mission-apprentissage/labonnealternance/issues/4762)).
