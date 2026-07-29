## Changelog : sante-psy (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur et la gestion des informations des psychologues et des étudiants. Des ajustements ont été apportés à l'annuaire des psychologues, à la prise de rendez-vous, et aux pages de connexion et de gestion de compte. Des améliorations de la documentation et de la clarté des informations ont également été réalisées.

### Évolutions fonctionnelles
- **Annuaire des psychologues :**
    - Suppression de l'adresse de l'objet de l'URL pour simplifier l'accès. [#864](https://github.com/betagouv/sante-psy/issues/864)
    - Utilisation des coordonnées géographiques lorsque disponibles pour une recherche plus précise. [#864](https://github.com/betagouv/sante-psy/issues/864)
    - Correction du tri aléatoire des résultats dans la base de données. [#867](https://github.com/betagouv/sante-psy/issues/867)
    - Possibilité pour les psychologues de modifier leur adresse. [#865](https://github.com/betagouv/sante-psy/issues/865)
- **Prise de rendez-vous :** Les psychologues ne peuvent plus proposer de nouveaux rendez-vous si la date n'a pas été modifiée. [#866](https://github.com/betagouv/sante-psy/issues/866)
- **Espace étudiant :**
    - Ajout d'un lien pour supprimer son compte via le support. [#869](https://github.com/betagouv/sante-psy/issues/869)
    - Affichage de l'adresse e-mail actuelle désactivée sur la page de modification du profil.
    - Avertissement indiquant que l'adresse e-mail ne peut être modifiée que si l'utilisateur est connecté.
- **Authentification :**
    - Amélioration de la formulation sur la page de connexion.
    - Redirection depuis `/espace-etudiant` vers `/login`.
- **Certificats :** Possibilité d'uploader des certificats. [#870](https://github.com/betagouv/sante-psy/issues/870)
- **Contact Support :** Amélioration de la formulation pour contacter le support. [#868](https://github.com/betagouv/sante-psy/issues/868)

### Évolutions techniques
- Correction de problèmes de linting. [#865](https://github.com/betagouv/sante-psy/issues/865)
- Mise en place d'un cron pour notifier les étudiants à 8h00.

### Autres changements
- Mise à jour de la formulation de la FAQ. [#867](https://github.com/betagouv/sante-psy/issues/867)
- Amélioration de la lisibilité des informations sur la page de connexion.
- Mise à jour des questions de la FAQ.
