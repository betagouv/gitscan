## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'analyse des justificatifs (fiches de paie, avis de situation), avec l'ajout de nouvelles fonctionnalités d'analyse automatique (Visale) et des corrections pour améliorer la précision et l'expérience utilisateur. Des améliorations ont également été apportées à la gestion des erreurs et à la navigation dans le formulaire de location.

### Évolutions fonctionnelles
- **Analyse des justificatifs :** Ajout de l'analyse automatique des documents Visale [#1912](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1912).
- **Fiche de paie :** Amélioration des messages d'erreur lors de l'analyse des fiches de paie [#1940](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1940).
- **Fiche de paie :** Ajout de l'analyse Doc-IA pour les fiches de paie [#1928](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1928).
- **Formulaire de location :** Remplacement du bouton "Sauvegarder" par un bouton "Suivant" sur la page d'explication de l'analyse [#1925](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1925).
- **Formulaire de location :** Amélioration de la validation du numéro DPE pour éviter les erreurs [#1917](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1917).
- **Formulaire de location :** Correction de l'affichage de la page de confirmation lorsque l'utilisateur est connecté [#1919](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1919).
- **Gestion des documents :** Correction pour masquer l'analyse Doc-IA lors de la mise à jour d'un fichier de salaire [#1935](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1935).
- **Upload de documents :** Amélioration de l'affichage des messages d'erreur lors de l'upload de documents (remplacement de la modal par un toast) [#1927](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1927) et ajout d'un message "asdir" [#1929](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1929).

### Évolutions techniques
- **Tests E2E :** Ajout de tests E2E pour la modal d'upload d'avis déclaratif [#1918](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1918).
- **Tests E2E :** Ajout d'un test happy path pour les fiches de paie [#1937](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1937).
- **Refactoring :** Refactorisation de la logique de sauvegarde des fichiers de salaire avec analyse [#1939](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1939).
- **Correction :** Correction du focus sur la somme lors du formulaire de salaire vide [#1941](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1941).
- **Correction :** Correction d'un bug empêchant de conserver la somme mensuelle après suppression d'un fichier de salaire [#1936](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1936).
- **Correction :** Correction d'un bug QA sur l'analyse des fiches de paie [#1942](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1942).
- **Correction :** Correction d'une faute de frappe sur le nom du garant [#1922](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1922).

### Autres changements
- **Documentation :** Mise à jour de la documentation pour les documents requis [#1920](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1920).
- **Versionning :** Publication des versions 3.5.2, 3.5.3 et 3.5.4.
- **Formulaire de contact :** Ajout d'un état de chargement au bouton de soumission du formulaire de contact [#1923](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1923).
- **Analyse des justificatifs :** Utilisation des données personnalisées des noms de taxes pour afficher les identités extraites [#1921](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1921).
