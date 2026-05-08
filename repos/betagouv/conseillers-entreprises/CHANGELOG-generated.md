## Changelog : conseillers-entreprises (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment via l'ajout de statistiques plus fines, la correction de problèmes d'accessibilité et l'amélioration de la gestion des données. Des efforts ont également été faits pour moderniser l'infrastructure et la configuration du projet.

### Évolutions fonctionnelles
- Ajout de nouvelles statistiques concernant les acquisitions d'entreprises et le temps de réponse. [#4446](https://github.com/betagouv/conseillers-entreprises/pull/4446)
- Possibilité de filtrer les experts par codes INSEE exclus. [#4454](https://github.com/betagouv/conseillers-entreprises/pull/4454)
- Amélioration du tri des réponses aux sujets dans l'administration. [#4462](https://github.com/betagouv/conseillers-entreprises/pull/4462)
- Ajout d'une nouvelle question sur la satisfaction des entreprises, avec la possibilité d'exporter les résultats en CSV. [#4392](https://github.com/betagouv/conseillers-entreprises/pull/4392)
- Affichage d'un questionnaire pour les utilisateurs, avec une modal et un élément de navigation dédié. [#4434](https://github.com/betagouv/conseillers-entreprises/pull/4434)
- Possibilité de modifier le statut des diagnostics. [#4435](https://github.com/betagouv/conseillers-entreprises/pull/4435)
- Ajout d'informations sur les statistiques pour les institutions. [#4410](https://github.com/betagouv/conseillers-entreprises/pull/4410)
- Mise à jour du domaine des emails vers `entreprises.service-public.gouv.fr`. [#4409](https://github.com/betagouv/conseillers-entreprises/pull/4409)

### Évolutions techniques
- Refactoring du code pour supprimer des méthodes inutilisées. [#4455](https://github.com/betagouv/conseillers-entreprises/pull/4455)
- Remplacement de Baleen par Ubika dans la documentation. [#4457](https://github.com/betagouv/conseillers-entreprises/pull/4457)
- Renommage de "CE" en "SPCE" dans le code et la documentation. [#4457](https://github.com/betagouv/conseillers-entreprises/pull/4457)
- Amélioration de la gestion des couleurs dans les paniers qualité. [#4401](https://github.com/betagouv/conseillers-entreprises/pull/4401)
- Mise à jour de Stimulus de 2.0.0 à 3.2.2. [#4433](https://github.com/betagouv/conseillers-entreprises/pull/4433)
- Mise à jour des dépendances : `erb`, `addressable`, `rack-session`. [#4428](https://github.com/betagouv/conseillers-entreprises/pull/4428), [#4404](https://github.com/betagouv/conseillers-entreprises/pull/4404), [#4405](https://github.com/betagouv/conseillers-entreprises/pull/4405)
- Amélioration de la performance en pré-calculant les flags de sollicitation. [#4439](https://github.com/betagouv/conseillers-entreprises/pull/4439)
- Refactorisation de la gestion des schémas SEO et intégration de données structurées plus complètes. [#4409](https://github.com/betagouv/conseillers-entreprises/pull/4409)

### Autres changements
- Correction de problèmes d'accessibilité liés au focus sur les champs de formulaire. [#4403](https://github.com/betagouv/conseillers-entreprises/pull/4403)
- Ajout d'un point manquant dans un texte. [#4402](https://github.com/betagouv/conseillers-entreprises/pull/4402)
- Suppression de code inutilisé (bandeau, support subject). [#4440](https://github.com/betagouv/conseillers-entreprises/pull/4440), [#4388](https://github.com/betagouv/conseillers-entreprises/pull/4388)
- Amélioration de la documentation et des commentaires dans le code.
- Correction de bugs mineurs et améliorations de la qualité du code.
