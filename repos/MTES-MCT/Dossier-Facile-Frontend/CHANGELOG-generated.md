## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 22 avril 2026)

### Résumé
Ce changelog présente les améliorations apportées à Dossier-Facile-Frontend au cours du dernier mois. Les principales évolutions concernent l'analyse de documents (notamment les fiches de paie et les avis de situation), l'expérience utilisateur sur les formulaires et la gestion des erreurs, ainsi que l'ajout de la fonctionnalité Visale.

### Évolutions fonctionnelles
- **Analyse de documents :**
    - Ajout de l'analyse des documents Visale [#1912](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1912).
    - Intégration d'un indicateur d'IA pour l'analyse des fiches de paie, avec affichage d'un message d'aide [#1948](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1948) et [#1928](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1928).
    - Amélioration des messages d'erreur liés à l'analyse des fiches de paie [#1940](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1940).
    - Masquage des documents actuels lorsque la liste est vide lors de l'analyse de la continuité de la fiche de paie [#1949](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1949).
- **Interface utilisateur :**
    - Ajout d'un lien vers la documentation dans le support de la location [#1950](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1950).
    - Ajout d'un badge d'erreur au composant de récapitulatif financier [#1947](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1947).
    - Suppression du bouton de réponse dans les messages lorsque le locataire est validé [#1943](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1943).
    - Refonte de la logique de sauvegarde des fichiers de salaire avec analyse [#1939](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1939).
    - Amélioration du focus sur la somme lorsque celle-ci est vide dans le formulaire de salaire [#1941](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1941).
    - Remplacement du modal "asdir" par un toast d'erreur lors du téléchargement [#1927](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1927).
    - Modification du bouton "Sauvegarder" par "Suivant" sur la page d'explication de l'analyse [#1925](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1925).
- **Formulaire de contact :**
    - Ajout d'un état de chargement au bouton de soumission du formulaire de contact [#1923](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1923).
- **Page de confirmation :**
    - Correction de la page de confirmation pour les utilisateurs connectés [#1919](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1919).

### Évolutions techniques
- **Compatibilité avec les règles fiscales :** Ajout de la compatibilité avec la règle des tranches d'imposition [#1946](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1946).
- **Tests E2E :** Ajout d'un test E2E pour le modal lors du téléchargement d'un avis déclaratif [#1918](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1918) et pour le happy path de l'analyse de la fiche de paie [#1937](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1937).
- **Refactoring :** Refactoring de la logique de sauvegarde des fichiers de salaire avec analyse.

### Autres changements
- Correction de fautes de frappe (garant) [#1922](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1922).
- Publication des versions 3.5.2, 3.5.3, 3.5.4 et 3.5.6.
