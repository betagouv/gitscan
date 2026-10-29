## Changelog : les-emplois (30 derniers jours, au 28 octobre 2026)

### Résumé
Ce mois a été marqué par une refonte majeure de l'expérience d'orientation (redesign pour data·inclusion) et une amélioration significative du suivi des usagers, notamment pour identifier les fins de parcours. Le système de gestion des dossiers employés a été profondément stabilisé et sécurisé, tandis que les performances de l'interface d'administration et la rapidité des tests ont été optimisées.

### Évolutions fonctionnelles
- **Orientation et parcours usagers** : 
    - Redesign complet du tunnel d'orientation et des pages de détails des services/structures.
    - Harmonisation terminologique : passage généralisé du terme "bénéficiaire" à "usager".
    - Ajout de nouveaux champs dans les formulaires (nationalité, âge) et d'un onglet "orientations" sur le profil de l'usager.
    - Intégration de badges visuels (QPV, fin de contrat, absence de poste ouvert).
- **Accompagnement et support** :
    - Mise en place d'un système de détection et de suivi des usagers en fin de contrat (filtres dédiés, propositions de demandes de support).
    - Création d'un nouveau module de "rapport de support professionnel" pour les employeurs IAE.
- **Recherche et interface** :
    - Ajout de formulaires de recherche directement sur la page d'accueil.
    - Amélioration de l'interface de connexion (nouveaux visuels, bandeau d'information DORA).
    - Optimisation de l'affichage des contrats et des informations de recherche usager.

### Évolutions techniques
- **Gestion des dossiers employés (Employee Record)** : 
    - Refonte complète du workflow (nouveaux états, transitions et gestion des erreurs de synchronisation avec ASP).
    - Sécurisation du processus d'upload (vérification des fichiers, verrouillage des objets).
- **Infrastructure et Performance** :
    - Migration du stockage de fichiers de MinIO vers RustFS.
    - Passage à Python 3.14.
    - Optimisation de l'administration Django (nouveaux paginateurs et mixins pour accélérer le chargement des grandes tables).
    - Amélioration de la CI/CD via le partitionnement des tests (sharding) et la mise en cache des bibliothèques spatiales.
- **Sécurité et Traçabilité** :
    - Accélération de l'enrôlement à la double authentification (MFA) pour les professionnels.
    - Renforcement de l'audit trail (suivi du navigateur, de l'IP et des callbacks d'authentification).
    - Amélioration de la fiabilité de la gestion des tâches de fond (reconnexion automatique à Redis).

### Autres changements
- **Nettoyage** : Suppression de code mort (Nexus), de fichiers statiques inutilisés et optimisation du CSS.
- **Documentation** : Mise à jour de la documentation technique, notamment sur l'audit trail.
