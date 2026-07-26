## Changelog : sante-psy (30 derniers jours, au 20 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment au niveau de l'annuaire des psychologues, de la gestion des rendez-vous et de l'espace étudiant. Des corrections de texte et des ajustements d'interface ont également été apportés pour une meilleure clarté et fluidité.

### Évolutions fonctionnelles
- **Annuaire des psychologues :**
    - Utilisation des coordonnées géographiques lorsque disponibles pour une recherche plus précise [#864](https://github.com/betagouv/sante-psy/issues/864).
    - Suppression de l'objet adresse des paramètres d'URL pour simplifier les liens [#862](https://github.com/betagouv/sante-psy/issues/862).
    - Possibilité pour les psychologues de modifier leur adresse [#865](https://github.com/betagouv/sante-psy/issues/865).
    - Amélioration de l'ordre des résultats dans l'annuaire (correction d'un problème de randomisation) [#867](https://github.com/betagouv/sante-psy/issues/867).
- **Rendez-vous :** Les psychologues ne peuvent plus proposer de nouveaux rendez-vous si la date n'a pas été modifiée [#866](https://github.com/betagouv/sante-psy/issues/866).
- **Espace étudiant :**
    - Ajout d'un lien pour supprimer son compte, redirigeant vers le support [#868](https://github.com/betagouv/sante-psy/issues/868).
    - Affichage de l'adresse e-mail actuelle désactivée dans la page de modification du profil.
    - Avertissement indiquant qu'il n'est possible de modifier l'e-mail que si l'utilisateur est connecté.
- **Connexion :** Amélioration du texte sur la page de connexion.
- **Notifications :** La tâche cron de notification des étudiants est maintenant exécutée à 8h00.
- **FAQ :** Mise à jour de la formulation de certaines questions et réponses.

### Évolutions techniques
- Refonte de l'utilisation des coordonnées dans l'annuaire pour une meilleure performance [#851](https://github.com/betagouv/sante-psy/issues/851).
- Correction de problèmes de linting.

### Autres changements
- Amélioration de la lisibilité des informations sur la page de connexion.
- Exclusion temporaire de tests DS défaillants pour permettre la poursuite du développement.
- Mise à jour de la redirection de l'espace étudiant vers la page de connexion.
