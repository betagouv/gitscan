## Changelog : gestion-eclairee (30 derniers jours, au 29 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'importation et le traitement des données financières, notamment pour les formats Factur-X et UBL Invoice. De plus, des améliorations ont été apportées à la gestion des téléchargements de fichiers et à la configuration de l'environnement.

### Évolutions fonctionnelles
- Ajout d'une vue pour télécharger les fichiers.
- Amélioration de la gestion des factures Factur-X.
- Support ajouté pour le format UBL Invoice 2.4, avec une robustesse accrue du traitement XML.
- Correction du mapping des services [#42223bc](https://github.com/betagouv/gestion-eclairee/issues/42223bc) et [#3c56ca7](https://github.com/betagouv/gestion-eclairee/issues/3c56ca7).
- Prise en compte des services à partir de l'annuaire CPRO.
- Ajout du test recette [#4db59b7](https://github.com/betagouv/gestion-eclairee/issues/4db59b7).
- Ajout du traitement budat et augdt pour l'export.

### Évolutions techniques
- Refactorisation de la gestion des téléchargements pour utiliser le stockage Django.
- Utilisation de Ruff pour le linting du code.
- Configuration du processus web en mode privé.
- Installation des librairies nécessaires pour cloakbrowser.
- Mise à jour du mapping des services.
- Suppression des anciennes versions des schémas XSD UBL-Invoice.

### Autres changements
- Forçage de la locale à "fr" pour les téléchargements [#a30e388](https://github.com/betagouv/gestion-eclairee/issues/a30e388).
- Travaux en cours (WIP) [#6349db4](https://github.com/betagouv/gestion-eclairee/issues/6349db4).
