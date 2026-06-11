## Changelog : labonnealternance (30 derniers jours, au 2026-06-10)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment sur le formulaire de candidature et la prise de rendez-vous avec les CFA. Des optimisations SEO ont été implémentées pour les pages métiers et villes, et des corrections ont été apportées pour améliorer la stabilité et la fiabilité de la plateforme. Des améliorations techniques ont également été réalisées concernant le logging, la gestion des erreurs et la configuration de l'environnement.

### Évolutions fonctionnelles
- **SEO :** Ajout de pages métiers optimisées pour le référencement ([#3222](https://github.com/mission-apprentissage/labonnealternance/issues/3222)).
- **Recherche :** Renommage du filtre "candidatures spontanées" en "entreprise à contacter" pour plus de clarté ([#4797](https://github.com/mission-apprentissage/labonnealternance/issues/4797)).
- **Smart Apply :** Application d'un seuil de 80 candidatures aux offres partenaires pour optimiser le processus ([#4799](https://github.com/mission-apprentissage/labonnealternance/issues/4799)).
- **Formulaire de candidature :** Amélioration de l'expérience utilisateur avec un défilement automatique vers le premier champ d'erreur et un focus sur celui-ci ([#4771](https://github.com/mission-apprentissage/labonnealternance/issues/4771)).
- **Prise de rendez-vous CFA :** Amélioration de l'UX du formulaire de prise de rendez-vous ([#4773](https://github.com/mission-apprentissage/labonnealternance/issues/4773)).
- **Handimatch :** Ajout du SIRET Handimatch pour une meilleure intégration ([#3171](https://github.com/mission-apprentissage/labonnealternance/issues/3171)).
- **CTA :** Modification des boutons d'appel à l'action (CTA) sur la page de dépôt d'offre ([#3136](https://github.com/mission-apprentissage/labonnealternance/issues/3136)).
- **Bloc salaire :** Mise à jour du bloc salaire sur les pages SEO ([#3213](https://github.com/mission-apprentissage/labonnealternance/issues/3213)).
- **Offres partenaires :** Suppression du champ `establishment_id` des offres partenaires ([#4767](https://github.com/mission-apprentissage/labonnealternance/issues/4767)).

### Évolutions techniques
- **Logging :** Unification du logging avec Pino, incluant la corrélation des identifiants de requête et l'enrichissement des logs HTTP ([#4800](https://github.com/mission-apprentissage/labonnealternance/issues/4800)).
- **Gestion des erreurs :** Ajout d'un `business error expired` pour tous les mappers ([#4740](https://github.com/mission-apprentissage/labonnealternance/issues/4740)).
- **Configuration :** Configuration du merge driver SOPS pour les fichiers d'environnement chiffrés ([#4736](https://github.com/mission-apprentissage/labonnealternance/issues/4736)).
- **CI/CD :** Envoi du changelog sur Slack après un déploiement en production ([#4723](https://github.com/mission-apprentissage/labonnealternance/issues/4723)).
- **Mise à jour :** Mise à jour de Next.js ([#4691](https://github.com/mission-apprentissage/labonnealternance/issues/4691)).
- **API :** Suppression de la route `/v1/application` et des schémas orphelins ([#4025](https://github.com/mission-apprentissage/labonnealternance/issues/4025)).
- **Suppression :** Suppression de Swagger et de ses dépendances de l'API v1 ([#4717](https://github.com/mission-apprentissage/labonnealternance/issues/4717)).
- **Refactoring :** Suppression de la collection `eligible_trainings_for_appointments_histories` et refactorisation de la tâche de nettoyage ([#4725](https://github.com/mission-apprentissage/labonnealternance/issues/4725)).

### Autres changements
- **Documentation :** Suppression des scripts Biome redondants et mise à jour de la documentation ([#4761](https://github.com/mission-apprentissage/labonnealternance/issues/4761)).
- **Configuration :** Génération d'un fichier `llms.txt` à la racine du site ([#4765](https://github.com/mission-apprentissage/labonnealternance/issues/4765)).
- **Templates d'issues :** Mise à jour des templates d'issues.
- **Migration :** Migration des références Jira vers GitHub Issues et ajout d'assets pour la migration des issues ([#4698](https://github.com/mission-apprentissage/labonnealternance/issues/4698)).
- **Blacklist CFA :** Mise à jour de la liste des CFA en blacklist ([#4689](https://github.com/mission-apprentissage/labonnealternance/issues/4689)).
- **Corrections mineures :** Diverses corrections de bugs et améliorations de la qualité du code.
