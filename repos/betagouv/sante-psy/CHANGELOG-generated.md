## Changelog : sante-psy (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des rendez-vous et l'ajout de nouvelles données. Les étudiants et les psychologues bénéficieront d'une meilleure expérience avec des indications claires sur la possibilité de supprimer des rendez-vous anciens et des informations plus complètes sur les établissements universitaires et les professionnels de santé. Une migration a également été effectuée pour ajouter le numéro RPPS aux informations des psychologues.

### Évolutions fonctionnelles
- **Rendez-vous :** Limitation du nombre de rendez-vous à 12 par étudiant [#850](https://github.com/betagouv/sante-psy/issues/850).
- **Rendez-vous :** Amélioration de l'expérience utilisateur lors de la création d'un nouveau rendez-vous : l'utilisateur reste sur la même page après l'ajout et le tableau des rendez-vous est mis à jour automatiquement [#841](https://github.com/betagouv/sante-psy/issues/841).
- **Rendez-vous :** Mise à jour du compteur de rendez-vous pour un étudiant, empêchant l'affichage d'une alerte rouge excessive [#841](https://github.com/betagouv/sante-psy/issues/841).
- **Suppression de rendez-vous :**  Les rendez-vous trop anciens ne peuvent plus être supprimés. Un bouton désactivé remplace le bouton de suppression, indiquant clairement cette limitation [#844](https://github.com/betagouv/sante-psy/issues/845). Un tooltip a été ajouté pour plus de clarté.
- **Universités :** La liste des universités françaises a été complétée [#845](https://github.com/betagouv/sante-psy/issues/845).
- **Psychologues :** Ajout du numéro RPPS aux informations des psychologues via une migration de base de données [#849](https://github.com/betagouv/sante-psy/issues/849).
- **Informations psychologue :** Renommage du champ "ADELI" en "ADELI/RPPS" dans la section d'informations du psychologue [#844](https://github.com/betagouv/sante-psy/issues/844).

### Évolutions techniques
- **Node.js :** Mise à jour de Node.js [#855](https://github.com/betagouv/sante-psy/issues/855).
- **Eslint :** Autorisation des exports uniques dans le code [#846](https://github.com/betagouv/sante-psy/issues/846).
- **Composant Tooltip :** Création d'un composant Tooltip réutilisable pour améliorer la clarté de l'interface utilisateur.
- **Université :** Ajout d'une colonne "uai" pour les universités [#846](https://github.com/betagouv/sante-psy/issues/846).

### Autres changements
- Rétrogradation temporaire d'une refactorisation de la création de nouveaux étudiants [#847](https://github.com/betagouv/sante-psy/issues/847).
- Amélioration de la largeur minimale des colonnes dans la vue des rendez-vous.
