## Changelog : sante-psy (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment au niveau de l'annuaire des psychologues, de la gestion des rendez-vous et de la simplification des actions pour les étudiants (modification d'email, suppression de compte). Des améliorations techniques ont également été apportées pour optimiser les notifications et l'infrastructure.

### Évolutions fonctionnelles
- **Annuaire des psychologues :**
    - Amélioration de l'utilisation des coordonnées géographiques pour la recherche [#864](https://github.com/betagouv/sante-psy/issues/864).
    - Suppression de `addressObject` des paramètres d'URL pour simplifier l'annuaire [#6530c4c](https://github.com/betagouv/sante-psy/commit/6530c4c).
    - Optimisation de la mémoire utilisée par l'annuaire [#851](https://github.com/betagouv/sante-psy/issues/851).
    - Possibilité pour les psychologues de modifier leur adresse [#865](https://github.com/betagouv/sante-psy/issues/865).
- **Rendez-vous :**
    - Un psychologue ne peut plus modifier un rendez-vous s'il n'a pas changé la date [#866](https://github.com/betagouv/sante-psy/issues/866).
- **Espace étudiant :**
    - Ajout d'un lien pour supprimer son compte et contacter le support.
    - Possibilité de modifier son adresse email. L'email actuel est affiché en lecture seule [#863](https://github.com/betagouv/sante-psy/issues/863).
    - Amélioration de la lisibilité des informations sur la page de connexion.
- **Notifications :**
    - Mise en place d'une tâche planifiée (cron job) pour notifier les étudiants chaque jour à 8h00 [#862](https://github.com/betagouv/sante-psy/issues/862).
- **Interface :**
    - Modification du texte du bouton "prendre rendez-vous" [#860](https://github.com/betagouv/sante-psy/issues/860).
    - Ajout d'un bouton de connexion sur le profil psychologue [#861](https://github.com/betagouv/sante-psy/issues/861).

### Évolutions techniques
- Mise à jour de Node.js [#855](https://github.com/betagouv/sante-psy/issues/855).
- Séparation du script pour exécuter la tâche planifiée de notification.
- Suppression d'un appel de fonction inutile dans le fichier de la tâche planifiée.

### Autres changements
- Mise à jour de la FAQ.
- Correction de problèmes de tri aléatoire dans la base de données.
- Amélioration de la lisibilité du code (linting).
- Exclusion temporaire de tests Cypress défaillants pour une correction ultérieure.
- Mise à jour de la dépendance axios (de 1.15.0 à 1.16.0) [#843](https://github.com/betagouv/sante-psy/issues/843).
