## Changelog : sante-psy (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment concernant la gestion des rendez-vous et la gestion du profil étudiant. Des corrections ont été apportées pour limiter le nombre de rendez-vous et empêcher la suppression de rendez-vous trop anciens. L'ajout du numéro RPPS pour les psychologues a également été implémenté.

### Évolutions fonctionnelles
- Les étudiants peuvent maintenant modifier leur adresse e-mail dans leur profil. [#863](https://github.com/betagouv/sante-psy/issues/863)
- Un bouton de connexion a été ajouté au profil psychologue. [#861](https://github.com/betagouv/sante-psy/issues/861)
- Le texte "Prendre rendez-vous" a été modifié pour une meilleure clarté. [#860](https://github.com/betagouv/sante-psy/issues/860)
- Les étudiants reçoivent désormais des notifications par cron job. [#862](https://github.com/betagouv/sante-psy/issues/862)
- Limitation du nombre de rendez-vous à 12 par étudiant. [#850](https://github.com/betagouv/sante-psy/issues/850)
- Les rendez-vous trop anciens ne peuvent plus être supprimés et le bouton de suppression est désactivé. [#845](https://github.com/betagouv/sante-psy/issues/845) et [#844](https://github.com/betagouv/sante-psy/issues/844)
- Amélioration de l'affichage des rendez-vous : ajout d'une info-bulle pour la suppression des rendez-vous.
- Lors de l'ajout d'un nouveau rendez-vous, l'utilisateur reste sur la même page et la table des rendez-vous est mise à jour.
- Lors de la suppression d'un rendez-vous, le compteur d'applications pour l'étudiant est mis à jour.
- La liste des universités a été mise à jour. [#845](https://github.com/betagouv/sante-psy/issues/845)

### Évolutions techniques
- Mise à jour de Node.js. [#855](https://github.com/betagouv/sante-psy/issues/855)
- Ajout du champ RPPS à la table des psychologues. [#849](https://github.com/betagouv/sante-psy/issues/849)
- Ajout d'une colonne "uai" à la table des universités. [#846](https://github.com/betagouv/sante-psy/issues/846)
- Refactorisation du code pour permettre la réutilisation d'un composant Tooltip.
- Modification de la configuration ESLint pour autoriser les exports uniques.
- Renommage du champ ADELI en ADELI/RPPS dans les informations du psychologue. [#965](https://github.com/betagouv/sante-psy/issues/965)

### Autres changements
- Correction temporaire de tests défaillants liés aux données de santé (DS).
- Reversion d'une modification concernant la création de nouveaux étudiants. [#847](https://github.com/betagouv/sante-psy/issues/847)
- Séparation du script pour exécuter la tâche cron de notification.
- Suppression d'un appel de fonction inutile dans le fichier cron.
- Correction d'un problème de largeur minimale des colonnes dans l'affichage des rendez-vous.
