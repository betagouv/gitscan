## Changelog : gestion-eclairee (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la mise en place de l'environnement Django et sur l'amélioration du processus de validation et d'importation des données CPRO (Comptes-rendus Prévisionnels d'Opérations). Des corrections ont été apportées pour gérer plus robustement les données, notamment en termes de formatage des montants et de gestion des erreurs liées aux champs obligatoires.

### Évolutions fonctionnelles
- Amélioration de la validation des données CPRO :
  - Gestion améliorée des arrondis pour les montants CPRO.
  - Validation de la longueur des codes EJ (Établissement Juridique).
  - Gestion plus robuste des champs "SERVICE" vides.
  - Exclusion de certains services/EJ spécifiques des vérifications.
- Mise à jour du motif de fichier CSV pour supporter l'absence du service et ajout d'une vérification de doublons.

### Évolutions techniques
- Initialisation du projet Django.
- Ajout des dépendances nécessaires au projet (Django, psycopg, pandas, mozilla-django-oidc).
- Mise en place de l'outil de formatage de code Ruff.
- Refactorisation des vérifications CPRO avec une meilleure gestion des nombres décimaux et un suivi de la progression.
- Implémentation du téléchargement des fichiers CPRO.

### Autres changements
- Première version du projet initialisée.
- Ajout d'une application Django initiale.
