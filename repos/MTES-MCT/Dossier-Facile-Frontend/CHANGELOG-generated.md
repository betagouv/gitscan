## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'analyse des justificatifs, notamment les fiches de paie et les avis de situation locative (Visale). Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment au niveau de la gestion des fichiers et des messages d'erreur. Plusieurs versions ont été publiées (3.5.0, 3.5.2, 3.5.3 et 3.5.4).

### Évolutions fonctionnelles
- **Analyse des justificatifs :** Ajout de l'analyse des documents Visale [#1912](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1912).
- **Fiche de paie :** Amélioration des messages d'erreur pour l'analyse des fiches de paie [#1940](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1940) et correction d'un bug lié à la suppression de fichiers de paie [#1936](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1936).  L'analyse Doc-IA est maintenant cachée lors de la modification d'un fichier de paie [#1935](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1935).
- **Avis déclaratif :** Ajout d'un test E2E pour la gestion du modal lors du téléchargement de l'avis déclaratif [#1918](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1918).
- **Documentation :** Mise à jour de la documentation pour les documents requis dans le contexte locatif [#1920](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1920).
- **Boutons et navigation :** Remplacement du bouton "Enregistrer" par un bouton "Suivant" après l'explication de l'analyse [#1925](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1925).
- **Formulaire de contact :** Ajout d'un état de chargement au bouton de soumission du formulaire de contact [#1923](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1923).
- **Validation DPE :** Ajout d'une validation pour empêcher la saisie d'un numéro DPE invalide [#1917](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1917).

### Évolutions techniques
- **Tests E2E :** Ajout d'un test E2E pour le cas d'utilisation de l'analyse de fiche de paie [#1937](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1937).
- **Refactoring :** Refactorisation de la logique de sauvegarde des fichiers de paie avec analyse [#1939](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1939).
- **Purge CSS :** Correction de la configuration de purge CSS pour désactiver la suppression des variables [#1914](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1914).
- **Gestion des erreurs :** Remplacement du modal "asdir" par un toast d'erreur lors du téléchargement [#1927](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1927) et ajout d'un message "asdir" dans la section de téléchargement [#1929](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1929).

### Autres changements
- Correction d'une faute de frappe concernant le garant [#1922](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1922).
- Correction d'un bug lié à la page de confirmation lorsque l'utilisateur est connecté [#1919](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1919).
- Limitation de la longueur des commentaires d'analyse [#1916](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1916).
- Correction d'un test E2E cassé [#1911](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1911).
- Correction d'un bug QA concernant l'analyse des fiches de paie [#1942](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1942).
- Correction d'un bug visale QA [#1926](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1926).
