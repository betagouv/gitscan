## Changelog : maestro (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des données, notamment pour les prélèvements, les analyses et les plans de surveillance. Des corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur, et de nouvelles fonctionnalités ont été implémentées, comme l'envoi de DAI par SFTP et l'intégration de Sentry pour le suivi des erreurs frontend. Des efforts ont également été consacrés à la modernisation de l'infrastructure et des dépendances du projet.

### Évolutions fonctionnelles
- Ajout de la possibilité d'envoyer des DAI (Demandes d'Intervention Analytique) via SFTP. [#698](https://github.com/betagouv/maestro/issues/698)
- Intégration de Sentry sur le frontend pour le suivi et la gestion des erreurs. [#768](https://github.com/betagouv/maestro/issues/768)
- Amélioration de la gestion des compétences analytiques des laboratoires (en cours de développement). [#491](https://github.com/betagouv/maestro/issues/491)
- Possibilité d'éditer les descripteurs des prélèvements. [#652](https://github.com/betagouv/maestro/issues/652)
- Ajout de la consultation du tableau de bord des plans fermés. [#696](https://github.com/betagouv/maestro/issues/696)
- Possibilité de filtrer les préleveurs par plan. [#667](https://github.com/betagouv/maestro/issues/667)
- Correction de l'affichage des décalages horaires. [#710](https://github.com/betagouv/maestro/issues/710)
- Correction de l'affichage de la note additionnelle sur les échantillons dans le suivi du prélèvement. [#780](https://github.com/betagouv/maestro/issues/780)
- Correction du lien de retour à la liste des prélèvements. [#779](https://github.com/betagouv/maestro/issues/779)
- Amélioration de l'affichage et de la gestion des plans de programmation, notamment pour les données DAOA. [#769](https://github.com/betagouv/maestro/issues/769)
- Correction de l'affichage du champ "Saisie" pour les DAOA.
- Correction de l'export des prélèvements. [#763](https://github.com/betagouv/maestro/issues/763)
- Ajout d'un message d'information quand aucune matrice programmée n'est disponible pour un plan de surveillance. [#781](https://github.com/betagouv/maestro/issues/781)

### Évolutions techniques
- Refactor du frontend pour typer les requêtes via les définitions des routes dans `shared`. [#693](https://github.com/betagouv/maestro/issues/693)
- Préparation à la migration vers PostgreSQL 17. [#708](https://github.com/betagouv/maestro/issues/708)
- Remplacement de ESLint et Prettier par BiomeJS pour le linting et le formattage du code. [#672](https://github.com/betagouv/maestro/issues/672)
- Correction de la gestion des erreurs pour les RAI (Requêtes d'Analyse Initiale). [#749](https://github.com/betagouv/maestro/issues/749)
- Amélioration des tests d'intégration pour accélérer l'exécution. [#724](https://github.com/betagouv/maestro/issues/724)

### Autres changements
- Correction de références et de noms de fichiers. [#783](https://github.com/betagouv/maestro/issues/783), [#715](https://github.com/betagouv/maestro/issues/715), [#744](https://github.com/betagouv/maestro/issues/744)
- Mise à jour de plusieurs dépendances (voir les commits pour la liste complète).
- Ajout de schémas pour les échanges hors EDI Sacha. [#711](https://github.com/betagouv/maestro/issues/711)
- Amélioration de la documentation de l'architecture. [#680](https://github.com/betagouv/maestro/issues/680)
- Correction de problèmes liés à l'injection des échantillons dans l'environnement de test. [#659](https://github.com/betagouv/maestro/issues/659)
- Correction de la récupération de l'utilisateur dans le local storage.
- Correction d'un bug empêchant l'enregistrement de données erronées lors de la saisie d'un prélèvement. [#706](https://github.com/betagouv/maestro/issues/706)
- Correction de l'affichage des plans de programmation. [#703](https://github.com/betagouv/maestro/issues/703)
- Correction du filtre par entreprise. [#755](https://github.com/betagouv/maestro/issues/755)
- Correction d'un problème de double appel API lors de la saisie d'un prélèvement. [#775](https://github.com/betagouv/maestro/issues/775)
- Correction d'un bug empêchant la validation de la programmation si la région l'avait déjà approuvée. [#738](https://github.com/betagouv/maestro/issues/738)
- Correction de l'affichage des résultats des résidus complexes. [#739](https://github.com/betagouv/maestro/issues/739)
- Correction d'un problème lié aux droits de saisie des informations d'expédition en DAOA. [#723](https://github.com/betagouv/maestro/issues/723)
- Correction d'un problème lié à l'affichage des plans de programmation non encore disponibles. [#669](https://github.com/betagouv/maestro/issues/669)
- Correction d'un bug empêchant la prise en compte du filtre pour les administrateurs. [#697](https://github.com/betagouv/maestro/issues/697)
- Correction d'un problème lié à la conformité des sigles pour Sigal. [#664](https://github.com/betagouv/maestro/issues/664)
- Si aucune détection, alors le résultat est "Conforme" et aucune notification n'est envoyée. [#754](https://github.com/betagouv/maestro/issues/754)
